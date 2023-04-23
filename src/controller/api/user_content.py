from logging import Logger

# AWS S3 import
import boto3
from boto3.resources.base import ServiceResource

# mongo imports
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Redis imports
import redis
from redis import Redis

# controller imports
from src.controller.exceptions import *

# model imports
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
            s3_creds (tuple): Should contain the following AWS S3 credentials:
                - uri (str): The URI of the database to connect to.
                - user (str): The username for the database.
                - password (str): The password for the database.

            mongo_uri (str): The URI of the database to connect to.
                Username and password should be included in the URI.

            redis_creds (tuple): Should contain the following Redis credentials:
                - host (str): The hostname of the database to connect to.
                - port (int): The port of the database.
                - password (str): The password for the database.

            logger (Logger): A Logger object.

        Returns:
            None.

        Exceptions:
            Throws a ConnectionValuesInvalidException if uri, user, or password is invalid for any of the databases.
        """
        # Credentials tuple destructuring
        s3_uri, s3_user, s3_password = s3_creds
        redis_host, redis_port, redis_password = redis_creds

        # TODO: Create a validator file for this
        # Validate input values
        if not (s3_uri and s3_user and s3_password):
            raise database_exceptions.ConnectionValuesInvalidException(
                s3_constants.NAME
            )
        if not mongo_uri:
            raise database_exceptions.ConnectionValuesInvalidException(
                mongo_constants.NAME
            )
        if not (redis_host and redis_port and redis_password):
            raise database_exceptions.ConnectionValuesInvalidException(
                redis_constants.NAME
            )

        self.s3: ServiceResource = self._connect_s3()
        self.mongo: MongoClient = self._connect_mongo(mongo_uri)
        self.redis: Redis = self._connect_redis(redis_host, redis_port, redis_password)

    def _connect_s3(
        self, s3_access_key: str, s3_secret_access_key: str
    ) -> ServiceResource:
        """Returns an AWS S3 Resource from the provided credentials."""
        return boto3.resource(
            "s3",
            aws_access_key_id=s3_access_key,
            aws_secret_access_key=s3_secret_access_key,
        )

    def _connect_mongo(self, mongo_uri: str) -> MongoClient:
        """Returns a Mongo client from the provided credentials."""
        return MongoClient(mongo_uri, server_api=ServerApi("1"))

    def _connect_redis(
        self, redis_host: str, redis_port: int, redis_password: str
    ) -> Redis:
        """Returns a Redis client from the provided credentials."""
        return redis.Redis(host=redis_host, port=redis_port, password=redis_password)
