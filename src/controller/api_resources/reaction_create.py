# Flask imports
from datetime import datetime
from json import dumps
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
from src.controller.validations.reaction_create_validation import (
    ReactionCreateValidator,
)

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.data_access.user_content import UserContent


class ReactionCreate(Resource):
    def __init__(
        self,
        user_content: UserContent,
        logger: Logger,
    ) -> None:
        """Instantiates a ReactionCreate API Resource for creating new posts.

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
        """Creates a new reaction from the provided reaction information in the request payload.

        Args:
            reaction_uri (str): The reaction image as a uri
            reactor_id: The reactor's netid
            post_id: The id of the post that the reaction belongs to

        Responses:
        """
        # Parse and validate request body
        try:          
            body: dict = ReactionCreateValidator().load(request.get_json())
            
            # Deconstruct body
            reaction_uri: str = body["reaction_uri"]
            reactior_id: str = body["reactor_id"]
            post_id: str = body["post_id"]
            reaction_datetime: int = int(datetime.now().timestamp())

            # Creates a reaction
            self.user_content.create_reaction(reaction_uri=reaction_uri, reactor_id=reactior_id, 
                                              post_id=post_id, datetime=reaction_datetime)
            
            
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

        return REACTION_CREATE_SUCCESS, status.HTTP_201_CREATED