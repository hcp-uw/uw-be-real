import boto3

s3 = boto3.resource("s3")

bucket = s3.Bucket("be-together")

# Example of uploading file
bucket.upload_file(Key="test.csv", Filename="./test.csv")

bucket.download_file(Key="test.csv", Filename="./test.csv")