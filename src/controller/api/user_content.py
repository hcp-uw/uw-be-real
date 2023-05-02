from logging import Logger
from datetime import timedelta

# Image decoding
import base64

# AWS S3 import
import boto3
from mypy_boto3_s3 import S3ServiceResource

# Mongo imports
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Redis imports
import redis
from redis import Redis

# Controller imports
from src.controller.exceptions import *
from src.controller.validations.credential_validation import *
from src.controller.validations.s3_validation import *

# Model imports
from src.model.classes.user import User
from src.model.constants import *
from src.model.queries import *


class UserContent:
    """The UserContent class is a Python API layer for AWS S3, MongoDB, and Redis.
    handling user contents (e.g. posts, images, etc.)"""

    def __init__(
        self,
        s3_creds: tuple[str, str],
        mongo_uri: str,
        redis_creds: tuple[str, str, str],
        logger: Logger,
    ) -> None:
        """Creates a new UserContent connected to AWS S3, MongoDB, Redis databases.

        Args:
            s3_creds (tuple): Should contain the following AWS S3 credentials in order:
                - aws_access_key_id (str): A valid AWS IAM user's access key id.
                - aws_secret_access_key (str): A valid AWS IAM user's secret access key.

            mongo_uri (str): The URI of the database to connect to.
                Username and password should be included in the URI.

            redis_creds (tuple): Should contain the following Redis credentials in order:
                - host (str): The hostname of the Redis database to connect to.
                - port (int): The port number of the Redis database.
                - password (str): The password for the Redis database.

            logger (Logger): A Logger object.

        Returns:
            None.

        Exceptions:
            Throws a ConnectionValuesInvalidException if database/storage credentials are invalid.
        """
        # Validate inputs
        validate_user_content_credentials(s3_creds, mongo_uri, redis_creds)

        # Connect database clients
        self.s3: S3ServiceResource = self._connect_s3(s3_creds)
        self.mongo: MongoClient = self._connect_mongo(mongo_uri)
        self.redis: Redis = self._connect_redis(redis_creds)

        # Logger
        self.logger: Logger = logger

    def _connect_s3(self, s3_creds: tuple[str, str]) -> S3ServiceResource:
        """Returns an AWS S3 Resource from the provided credentials."""
        s3_access_key, s3_secret_access_key = s3_creds
        return boto3.resource(
            "s3",
            aws_access_key_id=s3_access_key,
            aws_secret_access_key=s3_secret_access_key,
        )

    def _connect_mongo(self, mongo_uri: str) -> MongoClient:
        """Returns a Mongo client from the provided credentials."""
        return MongoClient(mongo_uri, server_api=ServerApi("1"))

    def _connect_redis(self, redis_creds: tuple[str, str, str]) -> Redis:
        """Returns a Redis client from the provided credentials."""
        redis_host, redis_port, redis_password = redis_creds
        return redis.Redis(host=redis_host, port=redis_port, password=redis_password)

    def _s3_upload_image(
        self,
        bucket_name: str,
        image_name: str,
        encoded_image: bytes,
        acl_perm: str = "public-read",
    ) -> str:
        """Uploads an image to a structured AWS S3 bucket.

        Args:
        - bucket_name (str): Name of S3 bucket.
            Available bucket names are:
            - tgr-us-west-0
            - tgr-us-west-1
            - tgr-us-west-2
            - tgr-us-west-3
            - tgr-us-west-4
            - tgr-us-west-5
            - tgr-us-west-6

        - image_name (str): file name of the image.
            The name must start with post_images/ or post_reactions/.
            Example: post_images/image.png or post_reactions/image.png

        - encoded_image (bytes): A Base64 encoded bytes-like image object.
        - acl_perm (str): ACL permission for the uploaded object.

        Returns:
            A str url of the uploaded image.

        Exceptions:
            Throws an InvalidS3BucketNameException if bucket_name is invalid.
            Throws an IncorrectFileExtensionTypeException if image_name is not a valid image file.
            Throws an InvalidS3AclPermissionException if the acl_perm is invalid.
        """
        # Validate arguments
        validate_s3_upload_image(bucket_name, image_name, acl_perm)

        # StackOverflow reference: https://stackoverflow.com/questions/43816346/most-efficient-way-to-upload-image-to-amazon-s3-with-python-using-boto3
        decoded_image = base64.b64decode(encoded_image)
        image_extension = image_name.split(".")[-1]

        # Upload image to S3
        # Could also use .upload_fileobj depending on how an image is read from Flask.
        self.s3.Bucket(bucket_name).put_object(
            key=image_name,
            Body=decoded_image,
            ContentType=f"image/{image_extension}",
            ACL=acl_perm,
        )

        # Generate an image url that expires in 7 days.
        image_url: str = self.s3.meta.client.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": bucket_name,
                "Key": image_name,
            },
            ExpiresIn=timedelta(days=7).total_seconds(),
        )

        return image_url

    def create_post(self, author: User, images: tuple, caption: tuple) -> None:
        """"""
        pass
