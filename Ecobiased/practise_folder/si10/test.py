from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import split, explode, col, year, month, dayofmonth
from pyspark.sql import SQLContext
from pyspark.sql import functions as F
from pyspark.sql import types

import sys
import os
import getopt
import subprocess
import time
import datetime
from datetime import datetime, date, timedelta
import subprocess as sp

from o9_de_utils.config_reader import ConfigReader
from o9_de_utils.de_utils import *
from dateutil.relativedelta import *

# Set up SparkContext
# sc = SparkContext.getOrCreate()
# Reduce Log noise
# sc.setLogLevel("ERROR")
# sqlContext = SQLContext(sc)
# spark = SparkSession(sc)
# spark.builder.appName("GetEarliestSellDate")
# spark.conf.set("spark.sql.sources.partitionOverwriteMode", "dynamic")

pos_daily_sales_path = None
earliest_sell_date_path = None
item_transition_path = None
earliest_sell_date_metadata_path = None
pos_metadata_path = None
store_list_path = None
run_mode = None
timezone = None

dummy_old_run_date = datetime.datetime.now() - timedelta(2)


def write_to_metadata():
    curr_ptt_metadata_ts_df = spark.createDataFrame([[datetime.datetime.now(), datetime.date.today()]], \
                                                    schema=types.StructType( \
                                                        [types.StructField("job_ts", types.TimestampType(), False), \
                                                         types.StructField("as_of_date", types.DateType(), False)]))
    curr_ptt_metadata_ts_df.write.partitionBy("as_of_date").option("header", "False").option("inferSchema",
                                                                                             "True").parquet(
        earliest_sell_date_metadata_path, mode='append')


def initialize(stack):
    global earliest_sell_date_path
    global item_transition_path
    global pos_daily_sales_path
    global earliest_sell_date_metadata_path
    global pos_metadata_path
    global timezone
    global run_mode
    global tenant_name
    global num_months
    global planning_group
    global store_list
    global store_list_path
    start_time = datetime.datetime.now()
    num_months = 36
    verbose = False
    stack = None
    # stack = 'pdev'
    # tenant_name = 'StarbucksCPR'
    verbose = False
    dry_run = False
    # run_mode = 'overwrite'
    # planning_group = 'ET'

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hsdp:v",
                                   ["help", "stack=", "dry-run", "py-files=", "timezone=", "run-mode=", "tenant-name=",
                                    "planning-group="])
    except getopt.GetoptError as err:
        print(str(err))
        # usage()
        sys.exit(2)

    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            # usage()
            sys.exit()
        elif o in ("-s", "--stack"):
            stack = a
        elif o in ("-d", "--dry-run"):
            dry_run = True
        elif o in ("-t", "--timezone"):
            timezome = a
        elif o in ("-r", "--run-mode"):
            run_mode = a
        elif o in ("-t", "--tenant-name"):
            tenant_name = a
        elif o in ("-pg", "--planning-group"):
            planning_group = a
        else:
            # assert False, "unhandled option"ii
            print("Ignoring unknown application option:{}".format(o))

    if not stack or not tenant_name:
        # usage()
        sys.exit(1)
    print("SUMMARY: Using stack <{}>".format(stack))
    print("Running for planning_group : {}".format(planning_group))
    # Read config
    # sys.path.append("../common")

    config = ConfigReader(stack, planning_group)

    pos_daily_sales_path = config.get_lsinput_tenant_dir(tenant_name, 'pos_daily_sales')
    earliest_sell_date_path = config.get_lsinput_tenant_dir(tenant_name, 'earliest_sell_date')
    item_transition_path = config.get_lsinput_tenant_dir(tenant_name, 'store_item_transition')
    pos_metadata_path = config.get_sbux_dir("pos_metadata")
    earliest_sell_date_metadata_path = config.get_lsinput_tenant_dir(tenant_name, 'earliest_sell_date_metadata')
    store_list_path = config.get_lsoutput_tenant_dir(tenant_name, 'storescopeaddandpublish')

    print("pos_daily_sales_path : %s" % pos_daily_sales_path)
    print("earliest_sell_date_path : %s" % earliest_sell_date_path)
    print("item_transition_path : %s" % item_transition_path)
    print("earliest_sell_date_metadata_path : %s" % earliest_sell_date_metadata_path)
    print("pos_metadata_path : %s" % pos_metadata_path)
    print("store_list_path : %s" % store_list_path)

    return config


def derive_dates():
    print("inside append mode")
    try:
        # sp.check_call(["hadoop", "fs", "-ls", earliest_sell_date_metadata_path])
        dbutils.fs.ls(earliest_sell_date_metadata_path)
        success = 0
    except:
        print("error")
        success = -1
        last_run_ts = None

    print("success " + str(success))

    if success == 0:
        earliest_sell_date_metadata_df = spark.read.parquet(earliest_sell_date_metadata_path)
        last_run_ts = earliest_sell_date_metadata_df.agg({"job_ts": "max"}).collect()[0][0]
    else:
        last_run_ts = dummy_old_run_date

    print("Earliest sell date last run time " + str(last_run_ts))

    pos_daily_metadata_table_df = spark.read.parquet(pos_metadata_path)
    print('printing pos_daily_sales_metadata')

    max_pos_run_ts = pos_daily_metadata_table_df.filter(col("job_ts") > last_run_ts) \
        .withColumnRenamed('as_of_date', 'as_of_date') \
        .select(F.col('as_of_date')) \
        .distinct()

    print('printing max_ts')
    max_pos_run_ts.show()
    date_list = [row['as_of_date'] for row in max_pos_run_ts.collect()]
    date_list = [x for x in date_list if x < datetime.date.today()]
    if len(date_list) == 0:
        print(
            "There is no record in pos metadata table to process since the last run date {} in earliest sell date metadata".format(
                last_run_ts))
        # exit()
        dbutils.notebook.exit(0)
    else:
        print('DeriveDates date_list : {}'.format(date_list))
        return date_list


def write_to_path(df, path, run_mode):
    # writing to target table
    # df.write.option("header", "False").option("inferSchema", "True"). \
    # option("timestampFormat", "YYYYMMDD").parquet(path, mode=mode)
    # path = '/mnt/cpr-o9/datalake/lsinput_5197/earliest_sell_date_test/planning_group={}'.format(planning_group.lower()),
    write_df(config, spark, df,
             schema="lsinput",
             entity="earliest_sell_date",
             tenant=tenant_name,
             header="False",
             format="parquet",
             inferSchema="True",
             mode=run_mode)


def get_earliest_date(df):
    # generating the minimum date in store item combination
    df_first_date = df.groupBy('store_number', 'item_number').agg(
        min(F.col('as_of_date')).alias('earliest_sell_date'))
    df_first_date = df_first_date.select(F.col('item_number').cast('long'), F.col('store_number').cast('long'),
                                         F.col('earliest_sell_date').cast('date'))
    return df_first_date


def earliest_sell_date(df_read_pos_sales, df_item_transition, df_earliest_sell_date, run_mode):
    df_pos_trans = df_read_pos_sales.join(broadcast(df_item_transition), on=['store_number', 'item_number'],
                                          how='left_outer')
    df_pos_trans = df_pos_trans.withColumn('item_number', F.when(F.col('item_number_new').isNotNull(), \
                                                                 F.col('item_number_new')).otherwise(
        F.col('item_number'))).drop('item_number_new')
    if run_mode == "append":
        df_read_pos_sales_new_items = df_pos_trans.select(F.col("item_number"), F.col("store_number")).subtract(
            df_earliest_sell_date.select(F.col("item_number"), F.col("store_number")))
        df_pos_trans = df_read_pos_sales_new_items.join(df_pos_trans, on=["item_number", "store_number"], how='inner')

    esd = get_earliest_date(df_pos_trans)
    return esd


def read_pos(df_store_list, date_list):
    print('reading data from {}'.format(pos_daily_sales_path))
    # if run_mode == 'overwrite':
    #     start_time = datetime.datetime.now()
    #     df_avail_posdaily = spark.read.parquet(pos_daily_sales_path) \
    #         .select(F.col('as_of_date')) \
    #         .filter((F.col('as_of_date') >= min_date.strftime("%Y-%m-%d")) & \
    #                 (F.col('as_of_date') <= max_date.strftime("%Y-%m-%d"))).distinct()
    #     avail_dt_pos = [row['as_of_date'] for row in df_avail_posdaily.collect()]
    #     # print(avail_dt_pos)
    #     pos_paths = [pos_daily_sales_path + "/as_of_date=" + date.strftime("%Y-%m-%d") for date in avail_dt_pos]
    # else:
    #     pos_paths = [pos_daily_sales_path + "/as_of_date=" + date.strftime("%Y-%m-%d") for date in date_list]
    avl_date_list = partition_check(pos_daily_sales_path, date_list)
    if not avl_date_list:
        print("\nThere are no dates available in pos_daily_sales to process")
        dbutils.notebook.exit(0)
    pos_paths = [pos_daily_sales_path + "/as_of_date=" + date.strftime("%Y-%m-%d") for date in avl_date_list]
    df_read_pos_sales = spark.read.option("basePath", pos_daily_sales_path).parquet(*pos_paths).filter(
        F.col("sales") > 0)
    df_read_pos_sales = df_read_pos_sales.join(broadcast(df_store_list), on='store_number', how='inner')  # added
    if len(df_read_pos_sales.head(1)) == 0:
        print('\n pos_daily_sales table does not contain data for dates :{} and store_list : {}'.format(date_list,
                                                                                                        store_list))
        dbutils.notebook.exit(0)
    return df_read_pos_sales


def read_item_transistion(df_store_list):
    print('reading data from {}'.format(item_transition_path))
    item_transition = spark.read.parquet(item_transition_path)
    df_item_transition = item_transition.select(item_transition.store_number, item_transition.item_number,
                                                item_transition.item_number_new)
    df_item_transition = df_item_transition.join(broadcast(df_store_list), on='store_number', how='inner')
    return df_item_transition


def get_store_list():
    # for planning group
    print('reading data from {}'.format(store_list_path))
    df_store_list = spark.read.parquet(store_list_path).select(F.col("location").alias('store_number')) \
        .filter((F.col("newlyentered") == "N") & (lower(F.col("planning_group")) == planning_group.lower())).distinct()

    store_list = [row['store_number'] for row in df_store_list.collect()]

    print("planning_group = {} and Store_list_count : {} ".format(planning_group, df_store_list.count()))
    return store_list, df_store_list


def partition_check(path, dt_list=[]):
    print("Input path :{} and datelist: {}".format(path, dt_list))
    avail_part_dt_list = []
    unavail_part_dt_list = []
    for dt in dt_list:
        # print(dt)
        full_path = path + "/as_of_date=" + dt.strftime("%Y-%m-%d")
        try:
            dbutils.fs.ls(full_path)
            avail_part_dt_list.append(dt)
        except:
            unavail_part_dt_list.append(dt)

    # print("Available partitons datelist: "+str(avail_part_dt_list))
    print("Unavailable partitons datelist: " + str(unavail_part_dt_list))
    return avail_part_dt_list


if __name__ == "__main__":
    spark = SparkSession.builder.appName("earliest_sell_date").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    start = time.time()
    config = initialize(sys.argv[1:])
    print("The job started at {}".format(start))
    print("The number of the arguments is {}".format(len(sys.argv)))
    print(sys.argv[1:])
    max_date = datetime.date.today() - datetime.timedelta(days=1)
    # min_date = datetime.date.today() + relativedelta(months=-int(num_months))
    # updated code to sync with test
    min_date = datetime.date.today() + relativedelta(months=-int(num_months)) - datetime.timedelta(days=1)
    # for picking dates
    if run_mode == 'overwrite':
        # min_date = spark.sql("select add_months('{0}',-36) as fmdt".format(max_date)).collect()[0]['fmdt']
        date_list = [(min_date + timedelta(days=n)) for n in range(int((max_date - min_date).days) + 1)]
        print('min date is:{}'.format(min_date))
        print('max date is:{}'.format(max_date))
        print('Date list : {}'.format(date_list))
        df_earliest_sell_date = None
        # date_list=None
    else:
        run_mode = "append"
        date_list = derive_dates()
        df_earliest_sell_date = spark.read.parquet(earliest_sell_date_path)

    print("The job is running in {} mode".format(run_mode))
    # reading pos data, item transition data and earliest sell date for the dates generated above
    store_list, df_store_list = get_store_list()
    if len(store_list) == 0:
        print('EXITING SINCE STORE_LIST IS EMPTY')
        dbutils.notebook.exit(0)
    # df_read_pos_sales = read_pos(min_date, max_date, date_list)
    df_read_pos_sales = read_pos(df_store_list, date_list)
    df_item_transition = read_item_transistion(df_store_list)
    esd = earliest_sell_date(df_read_pos_sales, df_item_transition, df_earliest_sell_date, run_mode)
    write_to_path(esd, earliest_sell_date_path, run_mode)
    write_to_metadata()

    end = time.time()
    print("The job ended at {}".format(end))
    delta = (end - start) / 60
    print("The time taken to run get_earliest_sell_date job is equal to {} minutes".format(delta))