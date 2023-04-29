# Regex matching
import re

# Controller imports
from src.controller.exceptions.generic_exceptions import *
from src.controller.exceptions.s3_exceptions import *

# Model imports
from src.model.constants.generic_constants import *
from src.model.constants.s3_constants import *


def validate_s3_upload_image(
    bucket_name: str,
    image_name: str,
    acl_perm: str,
) -> None:
    """Validates the inputs for private function s3_image_upload.

    Args:
        - bucket_name (str): Name of S3 bucket.
        - image_name (str): filename of the image.
        - acl_perm (str): ACL permission for the uploaded object.

    Returns:
        None.

    Exceptions:
        Throws an InvalidS3BucketNameException if bucket_name is invalid.
        Throws an IncorrectFileExtensionTypeException if image_name is not a valid image file.
        Throws an InvalidS3AclPermissionException if the acl_perm is invalid.
    """
    # Validate bucket name
    if bucket_name not in S3_BUCKETS:
        raise InvalidS3BucketNameException(bucket_name)

    # Validate image name
    if not re.match(IMAGE_EXTENSION_REGEX, image_name):
        raise IncorrectFileExtensionTypeException(
            f"Only {', '.join(ALLOWED_IMAGE_EXTENSIONS)} file types are allowed."
        )

    # Validate ACL permissions
    if acl_perm not in S3_ACL_PERMS:
        raise InvalidS3AclPermissionException(acl_perm)
