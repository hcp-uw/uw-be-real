# Model imports
from src.model.constants.s3_constants import *


class InvalidS3ProfileBucketNameException(Exception):
    """Raised when the given S3 bucket name is invalid."""

    def __init__(self, name: str) -> None:
        self.msg = f'"{name}" is not a valid AWS S3 bucket. Only {", ".join(S3_PROFILE_BUCKETS)} are valid S3 buckets.'

    def __str__(self) -> str:
        return self.msg


class InvalidS3PostBucketNameException(Exception):
    """Raised when the given S3 bucket name is invalid."""

    def __init__(self, name: str) -> None:
        self.msg = f'"{name}" is not a valid AWS S3 bucket. Only {", ".join(S3_POST_BUCKETS)} are valid S3 buckets.'

    def __str__(self) -> str:
        return self.msg


class InvalidS3AclPermissionException(Exception):
    """Raised when the given S3 ACL permission is invalid."""

    def __init__(self, name: str) -> None:
        self.msg = f'"{name}" is not a valid AWS S3 ACL Permission. Only {", ".join(S3_ACL_PERMS)} are valid S3 ACL permissions.'

    def __str__(self) -> str:
        return self.msg
