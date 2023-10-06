# Flask imports
from json import dumps
from bson import ObjectId, json_util
from flask import request
from flask_api import status
from flask_restful import Resource
from werkzeug.datastructures import FileStorage

# Logging and validation import
from logging import Logger
from marshmallow import ValidationError

# Utility imports
from datetime import datetime
from uuid import uuid4
from typing import Coroutine
from src.utilities.async_utils import (
    async_runner,
    async_wrapper,
)

# Controller imports
from src.controller.exceptions.neo4j_exceptions import (
    UserAlreadyExistsException,
    QueryFailureException,
)
from src.controller.exceptions.post_exceptions import *
from src.controller.exceptions.s3_exceptions import *
from src.controller.exceptions.generic_exceptions import *
from src.controller.validations.post_create_validator import (
    PostCreateValidator,
    validate_images,
)

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.constants.generic_constants import DATE_FORMAT
from src.model.data_access.user_content import UserContent

from datetime import datetime


class PostCreate(Resource):
    def __init__(
        self,
        user_content: UserContent,
        logger: Logger,
    ) -> None:
        """Instantiates a PostCreate API Resource for creating new posts.

        Methods:
            - POST

        Args:
            user_content (UserContent): A valid UserContent.

        Returns:
            None.
        """
        self.logger: Logger = logger
        self.user_content: UserContent = user_content

    def post(self) -> None:
        """Creates a new post from the provided post information in the request payload.

        Args:
            metadata (dict):
                author_id (str): The post author's UW NetID.
                location (str): An [optional] post location.

            content (dict):
                front_image (FileStorage): An front image encoded using multipart/form-data.
                back_image (FileStorage): An front image encoded using multipart/form-data.
                caption (str): A caption for the post.

        Responses:
        """
        # Parse and validate request body
        try:          
            body: dict = PostCreateValidator().load(request.get_json())
            
            # Deconstruct body
            metadata: dict = body["metadata"]
            content: dict = body["content"]
            author_id: str = metadata["author_id"]

            # Check if user has already made a post today
            # recent_post: str = self.user_content.get_user_post(author_id)
            # if recent_post:
            #     raise AlreadyPostedTodayException()

            # Get images
            images = content["file"]

            # Proceed to create post
            post_id: str = str(ObjectId())
            post_datetime: int = int(datetime.now().timestamp())
            default: str = ""
            caption: str = content.get("caption", default)
            location: str = metadata.get("location", default)
            is_global: bool = metadata["is_global"]

            # Upload post to AWS S3 and MongoDB
            # image_urls: tuple[str, str] = self.user_content.upload_post_images(
            #     post_id, images
            # )
            
            # Create the post in MongoDB
            self.user_content.create_post(author_id=author_id,
                                          post_id=post_id,
                                          caption=caption, location=location,
                                          is_global=is_global, image_urls=images,
                                          post_datetime=post_datetime)

            # Cache the post in Redis
            self.user_content.cache_post(author_id=author_id, is_global=is_global, post_id=post_id)
            
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST

        except InvalidImagesException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST

        except AlreadyPostedTodayException as e:
            return e.msg, status.HTTP_403_FORBIDDEN

        # This exception is unlikely to occur. 500 error instead of 400 because the
        # image extension should be validated already before getting to this point,
        # which means that this is likely to be an internal error.
        except IncorrectFileExtensionTypeException as e:
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        except InvalidS3PostBucketNameException as e:
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        return POST_CREATE_SUCCESS, status.HTTP_201_CREATED