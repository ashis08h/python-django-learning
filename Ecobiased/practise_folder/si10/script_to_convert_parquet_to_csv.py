import  pandas as pd


def parquet_to_csv(parquet_file_path, csv_file_path):
    df = pd.read_parquet(parquet_file_path)
    df.to_csv(csv_file_path, index=False)


if __name__ == '__main__':
    parquet_to_csv('class_code.parquet', 'class_code.csv')