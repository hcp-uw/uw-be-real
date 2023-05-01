NAME = "AWS S3"

# Enums
S3_BUCKETS = [
    "tgr-us-west-0",
    "tgr-us-west-1",
    "tgr-us-west-2",
    "tgr-us-west-3",
    "tgr-us-west-4",
    "tgr-us-west-5",
    "tgr-us-west-6",
]

# ACL permissions details here:
# https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html
S3_ACL_PERMS = [
    "private",
    "public-read",
    "public-read-write",
    "aws-exec-read",
    "authenticated-read",
    "bucket-owner-read",
    "bucket-owner-full-control",
    "log-delivery-write",
]
