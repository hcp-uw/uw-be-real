# Flask imports
from flask import request
from flask_api import status
from flask_restful import Resource

# Logging and validation import
from logging import Logger
from marshmallow import ValidationError

# Controller imports
from src.controller.exceptions.post_exceptions import *
from src.controller.exceptions.s3_exceptions import *
from src.controller.exceptions.generic_exceptions import *
from src.controller.validations.get_posts_validation import (
    GetPostsValidator,
)

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.constants.generic_constants import DATE_FORMAT
from src.model.data_access.user_content import UserContent


class GetPosts(Resource):
    def __init__(
        self,
        user_content: UserContent,
        logger: Logger,
    ) -> None:
        """Instantiates a GetPosts API Resource for getting new posts.

        Methods:
            - GET

        Args:
            user_content (UserContent): A valid UserContent.
            user_network (UserNetwork): A valid UserNetwork.

        Returns:
            None.
        """
        self.logger: Logger = logger
        self.user_content: UserContent = user_content

    def get(self) -> None:
        """Gets all the posts tailored to the specified feed request from

        Args:
            is_global (bool): Indicates whether to get posts from global or friends feed
            
        Responses:
        """
        # Parse and validate request body
        try:          
            body: dict = GetPostsValidator().load(request.args)
            
            # Deconstruct body
            is_global: bool = body["is_global"]

            # if is_global:
            posts = self.user_content.get_all_posts_global()
            
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST

        return posts, status.HTTP_200_OK