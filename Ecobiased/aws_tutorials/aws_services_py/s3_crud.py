# Import the boto3 library

import boto3

# Instantiate the boto3 for s3 and name your bucket.
s3 = boto3.resource('s3')
bucket_name = 'dct-crud-ls-1'

# check if bucket exists
# create the bucket if it does not exist

all_my_buckets = [bucket.name for bucket in s3.buckets.all()]
if bucket_name not in all_my_buckets:
    print(f"{bucket_name} does not exist, creating now...")
    s3.create_bucket(Bucket=bucket_name)
    print(f'{bucket_name} bucket has been created.')
else:
    print(f"{bucket_name} Bucket already exist, No need to create.")

# create 'file_1' and 'file_2'.
file_1 = 'file_1.txt'
file_2 = 'file_2.txt'

# upload 'file_1' to the new bucket.
s3.Bucket(bucket_name).upload_file(Filename=file_1, Key=file_1)
print(f"{file_1} has been uploaded to new bucket {bucket_name}")

# Read and print the file from bucket.

obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

# update 'file_1' in the bucket with new content from 'file_2'.

s3.Object(bucket_name, file_1).put(Body=open(file_2, 'rb'))

obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

# Delete the file from the bucket.

s3.Object(bucket_name, file_1).delete()
print(f"{file_1} has beed deleted from {bucket_name} Bucket.")

# Delete the bucket (Bucket should be empty).

bucket = s3.Bucket(bucket_name)
bucket.delete()
print(f'{bucket_name} Bucket has been deleted.')

