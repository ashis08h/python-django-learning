import pandas as pd


def convert_parquet_to_csv(parquet_file_path, csv_file_path):
    df = pd.read_parquet(parquet_file_path)
    df.to_csv(csv_file_path, index=False)


if __name__ == '__main__':
    convert_parquet_to_csv('parquet_file_path', 'csv_file_path')
