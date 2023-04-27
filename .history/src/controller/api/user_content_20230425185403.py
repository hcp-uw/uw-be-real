from logging import Logger

# AWS S3 import
import boto3
from boto3.resources.base import ServiceResource

# Mongo imports
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Redis imports
import redis
from redis import Redis

# Controller imports
from src.controller.exceptions import *
from src.controller.validations.user_content_validator import *

# Model imports
from src.model.classes import User
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
        validate_credentials(s3_creds, mongo_uri, redis_creds)

        # Connect database clients
        self.s3: ServiceResource = self._connect_s3(s3_creds)
        self.mongo: MongoClient = self._connect_mongo(mongo_uri)
        self.redis: Redis = self._connect_redis(redis_creds)

        self.logger: Logger = logger

    def _connect_s3(self, s3_creds: tuple[str, str]) -> ServiceResource:
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
    
    def create_post(self, author: User, images: tuple, caption: tuple) -> None:
        """
        """
        pass
