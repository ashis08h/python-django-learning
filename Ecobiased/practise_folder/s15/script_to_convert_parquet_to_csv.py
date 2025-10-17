import pandas as pd


def convert_parquet_to_csv(parquet_path, csv_path):
    df = pd.read_parquet(parquet_path)
    df.to_csv(csv_path)


if __name__ == '__main__':
    convert_parquet_to_csv("parquet_path", "csv_path")