from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import split, explode
from pyspark.sql.functions import col
from pyspark.sql.functions import *
from pyspark.sql.types import StructType
from pyspark.sql.types import *
from pyspark.sql.functions import explode, col
from pyspark.sql.window import Window
from pyspark.sql.functions import col, max, udf
from pyspark.sql import SQLContext
from datetime import datetime, timedelta, date
import pandas as pd
import numpy as np
import os
from itertools import repeat
import itertools
import warnings
# from prophet import Prophet
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing
# from croston import croston
from joblib import Parallel, delayed
import multiprocessing
from sklearn.linear_model import LinearRegression

warnings.filterwarnings('ignore')
from scipy import stats
import pyspark.sql.functions as F
from pyspark.sql.functions import pandas_udf, PandasUDFType
from pyspark.sql import SparkSession
from pyspark.sql.window import *
from dateutil.relativedelta import relativedelta
import pdb
from pyspark.sql.functions import col, upper
import pytz

import getopt
import subprocess
# sys.path.append("../common")
from o9_de_utils.config_reader import ConfigReader
from o9_de_utils.de_utils import *
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import split, explode
from pyspark.sql import SQLContext
from pyspark.sql.functions import col
from pyspark.sql.functions import *
from pyspark.sql.types import StructType
from pyspark.sql.types import *
from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number

import os
import getopt
import subprocess
import datetime
from datetime import datetime, date, timedelta
import pdb

# sys.path.append("../common")
from o9_de_utils.config_reader import ConfigReader
from o9_de_utils.de_utils import *

# sys.path.append("../common")
spark = SparkSession.builder.appName("StarbucksForecasting").getOrCreate()


def forecast_overidedata(stack,tenant_name, prediction_day, train_end_date):
    # Setup spark context
#     sc = SparkContext.getOrCreate()
    # Reduce log noise
    # sc.setLogLevel("ERROR")
#     sqlContext = SQLContext(sc)
#     spark = SparkSession(sc)
    # Read config
    config = ConfigReader(stack)
    # store_list = get_store_list(spark, config, tenant_name, planning_group).selectExpr("location as scslocationkey")
    # display(store_list)
    # input paths
    last_updated_ts_value = current_timestamp()
    shipment_segpath = config.get_aainput_dir(tenant_name, 'ReceiptsHistoryDaily')
    pos_segpath = config.get_aainput_dir(tenant_name, 'POSDailySalesNoTransType2')
    ItemSetupAssociationspath = config.get_aainput_dir(tenant_name, 'ItemSetupAssociations')
    longtermforecast_grpath = config.get_aaoutput_dir(tenant_name, 'non_aa_pre_national_guardrail_fcst_daily')
    shorttermforecast_grpath = config.get_aaoutput_dir(tenant_name, 'OPDemandTimeGranularity')
    finalstats_grpath = config.get_aaoutput_dir(tenant_name, 'periodicity_stats')
    # config.get_aaoutput_dir(tenant_name,"")+'_periodic / periodicity_stats'
    csv_path = config.get_aainput_dir(tenant_name, 'item_data')
    item_data = spark.read.parquet(csv_path).selectExpr("scsitemkey as sku",
                                                        "sku_classdesc",
                                                        "sku_deptdesc",
                                                        "sku_desc",
                                                        "sku_subclassdesc",
                                                        "sku_subdeptdesc",
                                                        "BrewCalendarEnabled",
                                                        "STFinalSKUType as ShipmentPOS").dropDuplicates()
    # display(item_data)
    # display()
    df2=read_files(spark, sql, config, entity=None, file_type="parquet", input_path=ItemSetupAssociationspath)\
    .withColumnRenamed("SCSItem2.[Item2]","swap_transitem").withColumnRenamed("ISAMGIsSwappable","swap").withColumnRenamed("ISAMGIsTransition","transition")\
    .selectExpr("scslocationkey","scsitemkey","case when swap=='true' then '1' else '0' end as swapflag","case when transition=='true' then '1' else '0' end as transitionflag","transition","swap_transitem")\
    .where("swapflag!='0' or transitionflag !='0'").drop("swapflag","transitionflag","transition").dropDuplicates()

    # Read pos data
    pos_df1 = read_files(spark, sql, config, entity=None, file_type="parquet", input_path=pos_segpath)
    pos_df2 = pos_df1.join(df2, on=["scslocationkey", "scsitemkey"], how="left").na.drop().drop("scsitemkey") \
        .withColumnRenamed("swap_transitem", "scsitemkey").select("scsitemkey", "timekey", "dailysalesnotranstypeqty2",
                                                                  "dailysalesnotranstypeamt2", "versionkey",
                                                                  "scslocationkey")
    pos_df = pos_df1.union(pos_df2)
    pos_df_agg = pos_df.groupBy("scsitemkey", "timekey") \
        .agg({'dailysalesnotranstypeqty2': 'sum'}) \
        .withColumnRenamed("sum(dailysalesnotranstypeqty2)", "sales_qty").withColumn("Source",
                                                                                     lit("pos")).withColumnRenamed(
        "timekey", "transaction_date").dropDuplicates()

    # Read shipment data

    shipment_df1 = read_files(spark, sql, config, entity=None, file_type="parquet", input_path=shipment_segpath)
    shipment_df2 = shipment_df1.join(df2, on=["scslocationkey", "scsitemkey"], how="left").na.drop().drop("scsitemkey") \
        .withColumnRenamed("swap_transitem", "scsitemkey").select("scsitemkey", "timekey", "receiptsquantity",
                                                                  "versionkey", "scslocationkey")
    shipment_df = shipment_df1.union(shipment_df2)
    shipment_df_agg = shipment_df.groupBy("scsitemkey", "timekey") \
        .agg({'receiptsquantity': 'sum'}) \
        .withColumnRenamed("sum(receiptsquantity)", "sales_qty").withColumn("Source",
                                                                            lit("shipments")).withColumnRenamed(
        "timekey", "transaction_date").dropDuplicates()
    # union of the pos and shipments
    pos_shipment_df = pos_df_agg.union(shipment_df_agg)

    # periodicity_stats data read and median
    periodicity_stats_inputdf = spark.read.parquet(finalstats_grpath)
    periodicity_stats = \
    periodicity_stats_inputdf.toPandas().groupby(
        ['scsitemkey'])['avg_perodicity_dates'].median().reset_index()
    periodicity_stats = spark.createDataFrame(periodicity_stats).selectExpr("scsitemkey",
                                                                            "avg_perodicity_dates as peridocity_computed")
    emp_RDD = spark.sparkContext.emptyRDD()
    # Create empty schema
    columns = StructType([StructField("sku", LongType(), True),
                          StructField("transaction_date", DateType(), True),
                          StructField("sources", StringType(), True),
                          StructField("salesqty", IntegerType(), True)])

    # Create an empty RDD with empty schema
    final_df_past_median = spark.createDataFrame(data=emp_RDD, schema=columns)
    periodicity_df = pos_shipment_df.join(periodicity_stats, on=['scsitemkey'], how='left').selectExpr("scsitemkey",
                                                                                                       "sales_qty",
                                                                                                       "transaction_date",
                                                                                                       "source",
                                                                                                       "case when peridocity_computed is null or peridocity_computed<21 then 21 else peridocity_computed end as peridocity_computed") \
        .groupBy("scsitemkey", "sales_qty", "transaction_date", "source", "peridocity_computed") \
        .agg({'sales_qty': 'sum'}).drop("sales_qty").withColumnRenamed("sum(sales_qty)", "sales_qty").orderBy(
        "transaction_date", ascending=False)

    # get the min date and maximum date ranegs for 20 days
    periodicity_df.createOrReplaceTempView("periodicity_df")
    pos_shipment_df.createOrReplaceTempView("pos_shipment_df")
    min_date = spark.sql(
        "select min(transaction_date) as min_transaction_date,max(transaction_date) as max_transaction_date from pos_shipment_df").collect()
    min_transaction_date = [row.min_transaction_date for row in min_date][0]
    max_transaction_date = [row.max_transaction_date for row in min_date][0]

    def generate_date_series(min_transaction_date, max_transaction_dates):
        return spark.createDataFrame([(min_transaction_date + datetime.timedelta(days=x),) for x in
                                      range(0, (max_transaction_date - min_transaction_date).days + 1)],
                                     ["transaction_date"])

    transaction_dates = generate_date_series(min_transaction_date, max_transaction_date).orderBy("transaction_date",
                                                                                                 ascending=False).withColumn(
        "temp", lit("1"))
    transaction_dates.createOrReplaceTempView("transaction_dates")
    mintransactiondate = min_transaction_date
    maxtransactiondate = max_transaction_date
    max_date = date_sub(to_date(current_timestamp()), 1)
    pos_shipment_dfs_source = pos_shipment_df.selectExpr("scsitemkey as sku", "Source as sources").dropDuplicates()

    dist_skus = periodicity_df.select(col('scsitemkey'), 'peridocity_computed').distinct().withColumn("temp", lit("1"))
    final_df_past_median = dist_skus.join(broadcast(transaction_dates), on=['temp'], how='left').drop("temp") \
        .withColumn('max_transactiondate', max_date).join(periodicity_df,
                                                          on=['scsitemkey', 'transaction_date', 'peridocity_computed'],
                                                          how='left') \
        .drop("source").na.fill(value=0, subset=["sales_qty"]) \
        .orderBy("transaction_date", ascending=False).withColumn("datesDiff", datediff(col("max_transactiondate"),
                                                                                       col("transaction_date"))) \
        .withColumn("peridocityday", expr("mod(datesDiff, peridocity_computed)").cast("int")) \
        .withColumn("days", expr("-peridocity_computed+peridocityday").cast("int")) \
        .withColumn('peridocitydate', expr("date_add(transaction_date,peridocityday)")) \
        .drop("days", "datesDiff", "transaction_date") \
        .selectExpr("scsitemkey as sku", "sales_qty", "peridocitydate as transaction_date") \
        .groupBy("sku", "transaction_date").agg({'sales_qty': 'sum'}).withColumnRenamed("sum(sales_qty)",
                                                                                        "salesqty").join(
        broadcast(pos_shipment_dfs_source), on=['sku'], how='left')

    items_data = item_data.selectExpr("sku", "sku_deptdesc")
    window_spec_transaction = Window.partitionBy('sku', 'store').orderBy(col('transactiondate').asc())
    final_predictions = spark.read.parquet(longtermforecast_grpath).selectExpr('versionkey', "scsitemkey as sku",
                                                                               'scslocationkey as store',
                                                                               "timekey",
                                                                               'SFSegmentationForecast as Predictions_Final',
                                                                               'RunDate as run_date')

    final_prediction = final_predictions.join(items_data, on=['sku'], how='left').dropDuplicates()

    final_prediction.createOrReplaceTempView("final_prediction")

    final_predictioned = spark.sql(
        "select *,from_unixtime(unix_timestamp(timekey, 'dd-MMM-yyyy'), 'yyyy-MM-dd') as transactiondate from final_prediction order by transactiondate") \
        .withColumn("timekey_rank", dense_rank().over(window_spec_transaction)).drop("timekey").select(
        'transactiondate', 'Predictions_Final', 'sku', 'sku_deptdesc', 'timekey_rank')
    final_predictions_df = final_predictioned.groupBy('transactiondate', 'sku', 'sku_deptdesc', 'timekey_rank').agg(
        {'Predictions_Final': 'sum'}).orderBy("transactiondate").withColumnRenamed("sum(Predictions_Final)",
                                                                                   "Predictions_final")

    # display(final_predictions_df)
    actuals_peridocity_median = periodicity_df.selectExpr("scsitemkey as sku", "peridocity_computed").dropDuplicates()
    final_predictions_df = final_predictions_df.join(actuals_peridocity_median, on='sku', how='left') \
        .withColumn("cycle", ceil(expr("timekey_rank/peridocity_computed"))) \
        .withColumn("Actuals_Forecast", lit('Forecast')).dropDuplicates()

    window_spec_transaction2 = Window.partitionBy('sku').orderBy(col('transaction_date').asc())
    final_df_past_median_filtered = final_df_past_median.selectExpr("sku", "transaction_date", "sources",
                                                                    "salesqty as Quantity",
                                                                    "'Actuals' as Actuals_Forecast") \
        .withColumn("cycle", dense_rank().over(window_spec_transaction2))
    final_df_past_median_filtered_cycle_max = final_df_past_median_filtered.groupBy("sku").agg(
        max("cycle")).withColumnRenamed("max(cycle)", "max_cycle")
    final_df_past_median_filtered_2 = final_df_past_median_filtered.join(final_df_past_median_filtered_cycle_max,
                                                                         on=['sku'], how='left').dropDuplicates()
    final_df_past_median_filtered_df = final_df_past_median_filtered_2.join(actuals_peridocity_median, on=['sku'],
                                                                            how='left').dropDuplicates()
    final_df_past_median_filtered_sku_agg = final_df_past_median_filtered_df.groupby('sku', 'transaction_date',
                                                                                     'Actuals_Forecast', 'cycle',
                                                                                     'peridocity_computed') \
        .agg({'Quantity': 'sum'}).withColumnRenamed("sum(Quantity)", "Quantity")

    final_df_past_median_filtered_temp = final_df_past_median_filtered_df.select('transaction_date', 'Quantity', 'sku',
                                                                                 'Actuals_Forecast', 'cycle')
    final_predictions_temp = final_predictions_df.selectExpr('transactiondate as transaction_date',
                                                             'Predictions_Final as Quantity', 'sku', 'Actuals_Forecast',
                                                             'cycle')
    combined_forecast_actuals = final_df_past_median_filtered_temp.union(final_predictions_temp).dropDuplicates()
    final_predictions_sku_agg = final_predictions_df.groupby('sku', 'cycle', 'Actuals_Forecast').agg(
        {'Predictions_Final': 'sum'}).withColumnRenamed("sum(Predictions_Final)", "Quantity")
    final_df_past_median_filtered_sku_agg = final_df_past_median_filtered_df.groupby('sku', 'cycle',
                                                                                     'Actuals_Forecast').agg(
        {'Quantity': 'sum'}) \
        .withColumnRenamed("sum(Quantity)", "Quantity")

    combined_forecast_actuals_sku_agg = final_df_past_median_filtered_sku_agg.union(
        final_predictions_sku_agg).dropDuplicates()

    # display(final_predictions_df)/
    final_df_past_median_filtered_sku_agg = final_df_past_median_filtered_sku_agg
    final_df_past_median_filtered_sku_aggs = final_df_past_median_filtered_sku_agg.where("cycle >1")
    final_predictions_sku_aggs = final_predictions_sku_agg.where(col("cycle").isin(['1', '2', '3', '4', '5']))
    # display(final_predictions_sku_aggs)
    data_cycle_actuals = final_df_past_median_filtered_sku_aggs.union(final_predictions_sku_aggs)
    data_cycle_actuals_new = data_cycle_actuals.selectExpr("*",
                                                           "case when Actuals_Forecast='Actuals' then Quantity else null end as Actuals",
                                                           "case when Actuals_Forecast='Forecast' then Quantity else null end as Forecast").orderBy(
        "cycle", "Actuals_Forecast")
    data_cycle_actuals_new.createOrReplaceTempView("data_cycle_actuals_new")
    # display(data_cycle_actuals_new)

    df = spark.sql(
        "select sku,sum(Actuals) as sum_Actuals,sum(Forecast) as sum_Forecast from data_cycle_actuals_new group by sku").where(
        "sum_Actuals >='0.0' and sum_Forecast >='0.0'").select("sku")
    data_cycle_actuals_final = data_cycle_actuals_new.join(df, on='sku', how='inner')

    #     dfs=data_cycle_actuals_final.toPandas()
    #     fcst = dfs.sort_values(by =['cycle'])['Forecast'].dropna().unique()[0]
    #     print(fcst)
    #     #display(data_cycle_actuals_final)

    def get_percentile_of_score(key, pdf):
        fcst = pdf.sort_values(by=['cycle'])['Forecast'].unique()[0]
        # print(fcst)
        # Calculate the percentile of the fcst value from history series
        percentile = stats.percentileofscore(pdf['Actuals'].dropna(), fcst)
        return pd.DataFrame([key + (percentile,)])

    final_write_df = data_cycle_actuals_final.groupBy(['sku']).applyInPandas(get_percentile_of_score,
                                                                             schema="scsitemkey string,percentile_score double").withColumn(
        'versionkey', lit('CurrentWorkingView')).withColumn("run_date",last_updated_ts_value)
    op_path = config.get_aaoutput_dir(tenant_name, 'skuforecast')
    spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")
    final_write_df.write.option("header", "False").option("inferSchema", "True").parquet(op_path, mode="overwrite")


def usage():
    print("Usage: python stg_item_rltd.py"
          " --stack <stack-name: unit-test|dev|test|cert|prod>"
          " --dry-run <optional. default=no dryrun>")
    return


def main(argv):
    start_time = datetime.datetime.now()
    tenant_name = None
    stack = None
    verbose = False
    dry_run = False
    prediction_day_yyyymmdd = None
    train_end_date = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hsdp:v",
                                   ["help", "stack=", "dry-run", "py-files=", "tenant-name=",
                                    "prediction-day-yyyymmdd=", "train-end-date="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-s", "--stack"):
            stack = a
        elif o in ("-d", "--dry-run"):
            dry_run = True
        elif o in ("-t", "--tenant-name"):
            tenant_name = a
        elif o in ("-t", "--prediction_day_yyyymmdd"):
            prediction_day_yyyymmdd = a
        elif o in ("-t", "--train_end_date"):
            train_end_date = a
        else:
            # assert False, "unhandled option"
            print("Ignoring unknown application option:{}".format(o))
    # ...
    if not stack or not tenant_name:
        usage()
        sys.exit(1)

    print("SUMMARY: Using stack <{}>".format(stack))

    # Run (load to raw)
    forecast_overidedata(stack, tenant_name, prediction_day_yyyymmdd, train_end_date)

    end_time = datetime.datetime.now()
    print("SUMMARY: stack <{}>".format(stack))
    # print("SUMMARY: Entity : {}".format(entity))
    print("SUMMARY: Total Time taken: {}".format(str(end_time - start_time)))

    return


if __name__ == "__main__":
    main(sys.argv[1:])