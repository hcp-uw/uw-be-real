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
from src.controller.validations.get_comments_reactions_validator import (
    GetCommentsReactionsValidator,
)

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.data_access.user_content import UserContent

class GetReactions(Resource):
    def __init__(
        self,
        user_content: UserContent,
        logger: Logger,
    ) -> None:
        """Instantiates a GetReactions API Resource for getting reactions.

        Methods:
            - GET

        Args:
            user_content (UserContent): A valid UserContent.

        Returns:
            None.
        """
        self.logger: Logger = logger
        self.user_content: UserContent = user_content

    def get(self) -> None:
        """Gets all the reactions from a post

        Args:
            post_id: The id of the post that the reactions belong to
            
        Responses:
        """
        # Parse and validate request body
        try:          
            body: dict = GetCommentsReactionsValidator().load(request.args)
            
            # Deconstruct body
            post_id: str = body["post_id"]

            reactions = self.user_content.get_all_reactions(post_id=post_id)
            
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST

        return reactions, status.HTTP_200_OK