# Time imports
from datetime import (
    timedelta,
    datetime,
)
import json

# Image typing
from werkzeug.datastructures import FileStorage

# AWS S3 import
import boto3
from mypy_boto3_s3 import S3ServiceResource

# Mongo imports
from pymongo.mongo_client import MongoClient
from pymongo.database import Database
from pymongo.server_api import ServerApi
import bson
from bson.objectid import ObjectId

# Redis imports
import redis
from redis import Redis

# Controller imports
from src.controller.exceptions import *
from src.controller.validations.credential_validation import *
from src.controller.validations.database_validation import *

# Model imports
from src.model.constants import *
from src.model.queries import *


class UserContent:
    """The UserContent class is a model layer for accessing AWS S3, MongoDB, and Redis
    to handle user contents (e.g. posts, images, etc.)"""

    def __init__(
        self,
        s3_creds: tuple[str, str],
        mongo_uri: str,
        redis_creds: tuple[str, str, str],
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

        Returns:
            None.

        Exceptions:
            Throws a ConnectionValuesInvalidException if database/storage credentials are invalid.
        """
        # Validate inputs
        validate_user_content_credentials(s3_creds, mongo_uri, redis_creds)

        # Connect database clients
        self.s3: S3ServiceResource = self._connect_s3(s3_creds)
        self.mongo_client: MongoClient = self._connect_mongo(mongo_uri)
        self.mongo: Database = self.mongo_client[mongo_constants.MONGO_DATABASE]
        self.redis: Redis = self._connect_redis(redis_creds)

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

    def _s3_upload_profile_image(
        self, bucket_name: str, image_name: str, image_file: FileStorage
    ) -> str:
        """Uploads a public-read user profile-related image to a structured AWS S3 bucket.

        Args:
        - bucket_name (str): Name of S3 bucket.
            Available bucket names are:
            - tgr-user-profile-us-west-0

        - image_name (str): file name of the image.
            The name must start with post_images/ or post_reactions/.
            Example: post_images/image.png or post_reactions/image.png

        - image_file (FileStorage): An image file received from a Flask API endpoint.

        Returns:
            A str url of the uploaded image.

        Exceptions:
            Throws an InvalidS3ProfileBucketNameException if bucket_name is invalid.
            Throws an IncorrectFileExtensionTypeException if image_name is not a valid image file.
        """
        # Validate arguments
        validate_s3_upload_profile_image(bucket_name, image_name)

        # Upload image to S3
        # put_object() is used over upload_fileobj() because the image is directly viewable
        # when put_object() is used, whereas upload_fileobj()'s image needs to be downloaded.
        image_extension = image_name.split(".")[-1]
        self.s3.Bucket(bucket_name).put_object(
            Key=image_name,
            Body=image_file,
            ContentType=f"image/{image_extension}",
            ACL=S3_PUBLIC_READ,
        )

        # Returns permanent image URL (unless removed)
        return f"https://{bucket_name}.s3.amazonaws.com/{image_name}"

    def _s3_upload_post_image(
        self, bucket_name: str, image_name: str, image_file: FileStorage
    ) -> str:
        """Uploads a user post-related image to a structured AWS S3 bucket.

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

        - image_file (FileStorage): An image file received from a Flask API endpoint.

        Returns:
            A str presigned-url of the uploaded image that expires (deletes) in 7 days.

        Exceptions:
            Throws an InvalidS3PostBucketNameException if bucket_name is invalid.
            Throws an IncorrectFileExtensionTypeException if image_name is not a valid image file.
        """
        # Validate arguments
        # validate_s3_upload_post_image(bucket_name, image_name)

        # Upload image to S3
        # put_object() is used over upload_fileobj() because the image is directly viewable
        # when put_object() is used, whereas upload_fileobj()'s image needs to be downloaded.
        image_extension = image_name.split(".")[-1]
        self.s3.Bucket(bucket_name).put_object(
            Key=image_name, Body=image_file, ContentType=f"image/{image_extension}"
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

    def upload_post_images(
        self, post_id: str, images: list[str]
    ) -> tuple[str, str]:
        """Uploads post content into AWS S3.

        Args:
            post_id (str): An unique post id.
            images (list): Contains [front image, back image].
                Image format must be compatible with werkzeug datastructures' FileStorage.

        Returns:
            A tuple of strings containing (front image url, back image url).
            The image urls are valid for up to 7 days. After 7 days, the image will be deleted.

        Exceptions:
            Throws an InvalidS3PostBucketNameException if bucket name is invalid.
            Throws an IncorrectFileExtensionTypeException if image name is not a valid image file.
        """
        # Determine which AWS S3 bucket this post belongs to based on weekday.
        # bucket_number: int = datetime.today().weekday()
        bucket_name: str = f"awstgr-us-west-1"

        # Get image extensions
        front_image, back_image = images
        # front_image_ext: str = front_image.split(".")[-1]
        # back_image_ext: str = back_image.split(".")[-1]
        front_image_ext: str = "jpg"
        back_image_ext: str = "jpg"
        # Create image file names based on post_id.
        front_image_path: str = f"{POSTS_FOLDER}/{post_id}-front.{front_image_ext}"
        back_image_path: str = f"{POSTS_FOLDER}/{post_id}-back.{back_image_ext}"

        # Upload images
        front_image_url: str = self._s3_upload_post_image(
            bucket_name=bucket_name, image_name=front_image_path, image_file=front_image
        )
        back_image_url: str = self._s3_upload_post_image(
            bucket_name=bucket_name, image_name=back_image_path, image_file=back_image
        )
        return front_image_url, back_image_url

    def cache_post(self, author_id: str, post_id: str, is_global: bool) -> None:
        """Caches a post in Redis."""
        cache_post_info = {
            "post_id": post_id,
            "is_global": is_global
        }
        self.redis.hset(name=author_id, key=author_id, value=json.dumps(cache_post_info))
        self.redis.expire(name=author_id, time=timedelta(hours=24))

    def create_post(
        self,
        post_id: str,
        author_id: str,
        caption: str,
        location: str,
        is_global: bool,
        image_urls: tuple[str, str],
        post_datetime: str
    ) -> None:
        """Creates a post and its related documents in MongoDB.

        Args:

        Returns:

        Exceptions:

        """
        post_document = {
            "_id": post_id,
            "author_id": author_id,
            "front_image": image_urls[0],
            "back_image": image_urls[1],
            "caption": caption,
            "location": location,
            "is_global": is_global,
            "datetime": post_datetime,
        }

        comments_document = {
            "_id": post_id,
            "comments": [],
        }

        reactions_document = {
            "_id": post_id,
            "reactions": [],
        }

        # Insert documents into MongoDB collections
        self.mongo[mongo_constants.POSTS_COLLECTION].insert_one(post_document)
        self.mongo[mongo_constants.COMMENTS_COLLECTION].insert_one(comments_document)
        self.mongo[mongo_constants.REACTIONS_COLLECTION].insert_one(reactions_document)

    def get_user_post(self, netid: str) -> dict | None:
        """Returns a user's daily post as a dict of post information from Redis.

        Args:
            netid (str): The user's UW NetID.

        Returns:
            A dict of post information. If the user has not made a post, None is returned.
        """
        return self.redis.hgetall(netid)

    def get_all_posts_global(self):
        """Returns all the posts in Redis"""
        posts = []
        # For the sake of the demo we display all the posts
        for post in self.mongo[mongo_constants.POSTS_COLLECTION].find({}): 
            posts.append(post)

        # Formal code for redis being a cache
        # for key in self.redis.scan_iter():
        #     user_to_post_info = self.get_user_post(key)
        #     post_info_dict = json.loads(user_to_post_info.get(key).decode('utf-8'))
        #     curr_post_id = post_info_dict.get("post_id")
        #     post = self.mongo[mongo_constants.POSTS_COLLECTION].find_one({"_id": curr_post_id})
        #     posts.append(post)
        return posts