NAME = "AWS S3"
POSTS_FOLDER = "post_images"
REACTIONS_FOLDER = "post_reactions"
PROFILE_FOLDER = "profile"

# Constants
# S3_PROFILE_BUCKETS = [
#     "tgr-user-profile-us-west-0",
# ]
# S3_POST_BUCKETS = [
#     "tgr-us-west-0",
#     "tgr-us-west-1",
#     "tgr-us-west-2",
#     "tgr-us-west-3",
#     "tgr-us-west-4",
#     "tgr-us-west-5",
#     "tgr-us-west-6",
# ]

# For the sake of scope, we will only use a single bucket for both profile and post images
S3_POST_BUCKETS = [
    "awstgr-us-west-1"
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

S3_PUBLIC_READ = "public-read"
