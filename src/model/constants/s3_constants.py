NAME = "AWS S3"

# Enums
S3_BUCKETS = []

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
