# method 1 using pandas and loop

import pandas as pd

df = pd.read_parquet("bigfile.parquet")

chunksize = 100_000

for i in range(0, len(df), chunksize):
    chunk = df.iloc[i:i+chunksize]
    chunk.to_parquet(f"chunk_{i//chunksize + 1}.parquet", index=False)

# method 2

import dask.dataframe as dd

# dd.read_parquet() does not read data immediately it builds a computation graph
df = dd.read_parquet("bigfile.parquet")

# df.repartition() instructs dask to split the file into multiple logical partitions (chunks)

df = df.repartition(partition_size="100MB")

"""
df.to_partition() then triggers execution:
It launches background tasks
reads chunk of data
"""

df.to_parquet("output_chunks/", write_index=False)