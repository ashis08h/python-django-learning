import pandas as pd

def parquet_to_csv(parquet_file, csv_file):
    # Read the Parquet file into a pandas DataFrame
    df = pd.read_parquet(parquet_file)

    # Write the DataFrame to a CSV file
    df.to_csv(csv_file, index=False)

if __name__ == "__main__":
    parquet_file = "class_code_assign.parquet"
    csv_file = "class_code_assign.csv"
    parquet_to_csv(parquet_file, csv_file)