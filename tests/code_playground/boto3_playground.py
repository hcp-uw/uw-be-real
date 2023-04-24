import os
from dotenv import load_dotenv

import boto3

BUCKET_NAME = "tgr-us-west-0"

# load secrets
aws_env_path = os.path.join(os.getcwd(), "secrets", "aws_s3", ".env")
load_dotenv(aws_env_path)

access_key = os.getenv("ACCESS_KEY")
secret_access_key = os.getenv("SECRET_ACCESS_KEY")

# Retrieve the list of existing buckets
s3 = boto3.resource(
    "s3", aws_access_key_id=access_key, aws_secret_access_key=secret_access_key
)
for bucket in s3.buckets.all():
    print(bucket.name)

# Output the bucket names
# print('Existing buckets:')
# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')
