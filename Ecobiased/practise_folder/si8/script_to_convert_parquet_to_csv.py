import pandas as pd


def convert_parquet_to_csv(parquet_file, csv_file):
    # read parquet file.
    df = pd.read_parquet(parquet_file)

    #write to csv file.
    df.to_csv(csv_file, index=False)


if __name__=='__main__':
    convert_parquet_to_csv('class_code.parquet', 'class_code.csv')