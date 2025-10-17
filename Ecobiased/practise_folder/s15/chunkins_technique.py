import pandas as pd

# method 1 use of pandas and loop
df = pd.read_parquet("path_to_parquet.csv")
chunk_size = 10_000
for i in range(0, len(df), chunk_size):
    chunk = df.iloc[i, i+chunk_size]
    chunk.to_parquet(f"chunk{i//chunk_size + 1}.parquet", index=False)


# method 2 use of dask

import dask.dataframe as dd

# dd.read_parquet() does not read data immediately it builds a computation graph
df = dd.read_parquet('bigfile.parquet')

# df.repartition() instructs dask to split the file into multiple logical partitions (chunk)
df = df.repartition(partition_size='100MB')

# df.to_partition then trigger execution
# It launches background tasks
# read chunk of data.
df.to_partition('output_chunks/', write_index=False)