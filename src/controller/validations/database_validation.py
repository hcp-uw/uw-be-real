# Regex matching
import re

# Controller imports
from src.controller.exceptions.generic_exceptions import *
from src.controller.exceptions.s3_exceptions import *

# Model imports
from src.model.constants.generic_constants import *
from src.model.constants.s3_constants import *


def validate_s3_upload_profile_image(bucket_name: str, image_name: str) -> None:
    """Validates the inputs for private function s3_image_upload.

    Args:
        - bucket_name (str): Name of S3 bucket.
        - image_name (str): filename of the image.

    Returns:
        None.

    Exceptions:
        Throws an InvalidS3BucketNameException if bucket_name is invalid.
        Throws an IncorrectFileExtensionTypeException if image_name is not a valid image file.
    """
    # Validate bucket name
    if bucket_name not in S3_PROFILE_BUCKETS:
        raise InvalidS3ProfileBucketNameException(bucket_name)

    # Validate image name
    if not re.match(PROFILE_IMAGE_EXTENSION_REGEX, image_name):
        raise IncorrectFileExtensionTypeException(
            f"The image name must begin with post_images/ or post_reactions/ and have {', '.join(ALLOWED_IMAGE_EXTENSIONS)} file types."
        )


def validate_s3_upload_post_image(bucket_name: str, image_name: str) -> None:
    """Validates the inputs for private function s3_image_upload.

    Args:
        - bucket_name (str): Name of S3 bucket.
        - image_name (str): filename of the image.

    Returns:
        None.

    Exceptions:
        Throws an InvalidS3BucketNameException if bucket_name is invalid.
        Throws an IncorrectFileExtensionTypeException if image_name is not a valid image file.
    """
    # Validate bucket name
    if bucket_name not in S3_POST_BUCKETS:
        raise InvalidS3PostBucketNameException(bucket_name)

    # Validate image name
    if not re.match(POST_IMAGE_EXTENSION_REGEX, image_name):
        raise IncorrectFileExtensionTypeException(
            f"The image name must begin with post_images/ or post_reactions/ and have {', '.join(ALLOWED_IMAGE_EXTENSIONS)} file types."
        )
