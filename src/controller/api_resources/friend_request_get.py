# Flask imports
from flask import request
from flask_api import status
from flask_restful import Resource

# Logging and validation import 
from logging import Logger
from marshmallow import ValidationError

# Controller imports
from controller.exceptions.generic_exceptions import NoInputsException
from controller.exceptions.user_exceptions import UserNotFoundException
from controller.validations.user_profile_validator import UserProfileValidator

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.data_access.user_network import UserNetwork

class FriendRequestGet(Resource):
    def __init__(self, user_network: UserNetwork, logger: Logger) -> None:
        """Instantiates a FriendRequestGet API Resource for retrieving user's friend request information.

        Methods:
            - GET

        Args:
            user_network (UserNetwork): A valid UserNetwork.

        Returns:
            None.
        """
        self.logger: Logger = logger
        self.user_network: UserNetwork = user_network
    
    def get(self):
        """Get user's incoming friends requests from the provided information in the request payload.

        Args:
            netid (str): The UW NetID of the user.

        Returns:
            Serialized JSON data of the user's friends.

        Responses:
            200 OK:
                - User's incomin friend requets successfully retrieved.
            400 BAD REQUEST:
                - Invalid request, no changes made.
            500 INTERNAL SERVER ERROR:
                - Generic error.
        """
        # Parse and validate request body
        try:
            body: dict = UserProfileValidator().load(request.args)
            netid = body["netid"]
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST
        
        #Query Database        
        try:
            user_info: dict = self.user_network.get_user(netid)
            if not user_info:
               raise UserNotFoundException(netid) 
        

            friend_info: list[str] = self.user_network.get_incoming_friend_requests(netid)

        
        # Return response
        except NoInputsException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except UserNotFoundException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except Exception as e:
            self.logger.log(ERROR, str(e))
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        return friend_info, status.HTTP_200_OK
 