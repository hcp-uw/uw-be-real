# Flask imports
from flask import request
from flask_api import status
from flask_restful import Resource

# Logging and validation import 
from logging import Logger
from marshmallow import ValidationError
from controller.exceptions.friend_exceptions import NotFriendsException

# Controller imports
from controller.exceptions.generic_exceptions import NoInputsException
from controller.exceptions.user_exceptions import CannotPerformOnSelfException, UserNotFoundException
from controller.validations.friend_request_validator import FriendRequestSendValidator

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.data_access.user_network import UserNetwork

class UserBlock(Resource):
    def __init__(self, user_network: UserNetwork, logger: Logger) -> None:
        """Instantiates a UserBlock API Resource for a user to block another user

        Methods:
            - POST

        Args:
            user_network (UserNetwork): A valid UserNetwork.

        Returns:
            None.
        """
        self.logger: Logger = logger
        self.user_network: UserNetwork = user_network
    
    def post(self):
        """Block another user.

        Args:
            sender_netid (str): The UW NetID of the user sending the block
            recipient_netid (str): The UW NetID of the user receiving the block


        Responses:
            200 OK:
                - Successfully blocked
            400 BAD REQUEST:
                - Invalid request, no changes made.
            500 INTERNAL SERVER ERROR:
                - Generic error.
        """
        # Parse and validate request body
        try:
            body: dict = FriendRequestSendValidator().load(request.get_json())
            sender_netid = body["sender_netid"]
            recipient_netid = body["recipient_netid"]
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST
        
        #Query Database
        try:
            if sender_netid == recipient_netid: 
                raise CannotPerformOnSelfException(sender_netid)
            if not self.user_network.get_user(sender_netid):
                raise UserNotFoundException(sender_netid)
            if not self.user_network.get_user(recipient_netid):
                raise UserNotFoundException(recipient_netid)
            print("h")

            self.user_network.block_user(sender_netid, recipient_netid)
        # Return response
        except NoInputsException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except UserNotFoundException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except CannotPerformOnSelfException as e: 
            return e.msg, status.HTTP_400_BAD_REQUEST
        except Exception as e:
            self.logger.log(ERROR, str(e))
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        return status.HTTP_200_OK
 