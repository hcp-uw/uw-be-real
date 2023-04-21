from logging import Logger
# AWS S3 import
import boto3
from mypy_boto3_s3.client import S3Client
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
    def __init__(self, 
                 s3_creds: tuple[str, str, str], 
                 mongo_creds: tuple[str, str, str], 
                 redis_creds: tuple[str, str, str],
                 logger: Logger) -> None:
        """Creates a new UserContent connected to AWS S3, MongoDB, Redis databases.

        Args:
            s3_creds (tuple): Should contain the following AWS S3 credentials :
                - uri (str): The URI of the database to connect to.
                - user (str): The username for the database.
                - password (str): The password for the database.

            mongo_creds (tuple): Should contain the following mongo credentials:
                - uri (str): The URI of the database to connect to.
                - user (str): The username for the database.
                - password (str): The password for the database.

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
        mongo_uri, mongo_user, mongo_password = mongo_creds
        redis_host, redis_port, redis_password = redis_creds

        # TODO: Create a validator file for this
        # Validate input values
        if not (s3_uri and s3_user and s3_password):
            raise database_exceptions.ConnectionValuesInvalidException(s3_constants.NAME)
        
        if not (mongo_uri and mongo_user and mongo_password):
            raise database_exceptions.ConnectionValuesInvalidException(mongo_constants.NAME)
        
        if not (redis_host and redis_port and redis_password):
            raise database_exceptions.ConnectionValuesInvalidException(redis_constants.NAME)
        
        # TODO: Connect to AWS S3
        self.s3_driver: S3Client = self._connect_s3()

        # TODO: Connect to MongoDB
        self.mongo_driver = None

        # TODO: Connect to Redis
        self.redis_driver = self._connect_redis(redis_host, redis_port, redis_password)

    def _connect_s3(self) -> None:
        s3_client: S3Client = boto3.client('s3')

    def _connect_mongo(self) -> None:
        pass

    def _connect_redis(self, 
                       redis_host: str, 
                       redis_port: int,
                       redis_password: str) -> Redis:
        return redis.Redis(
            host=redis_host,
            port=redis_port,
            password=redis_password
        )