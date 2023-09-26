# Flask imports
from flask import request
from flask_api import status
from flask_restful import Resource

# Logging and validation import 
from logging import Logger
from marshmallow import ValidationError
from controller.exceptions.friend_exceptions import NoFriendRequestException, NotFriendsException

# Controller imports
from controller.exceptions.generic_exceptions import NoInputsException
from controller.exceptions.user_exceptions import UserNotFoundException
from controller.validations.friend_request_validator import FriendRequestRespondValidator

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.data_access.user_network import UserNetwork

class FriendRequestRespond(Resource):
    def __init__(self, user_network: UserNetwork, logger: Logger) -> None:
        """Instantiates a FriendRequestRespond API Resource for a user to 
        respond to a friend request, either accepting or denying it.

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
        """Accepts or denies a user's incoming friend request in the request payload.

        Args:
            sender_netid (str): The UW NetID of the user sending the friend removal
            recipient_netid (str): The UW NetID of the user receiving the friend removal


        Responses:
            200 OK:
                - Successfully accepted or denied the friend request
            400 BAD REQUEST:
                - Invalid request, no changes made.
            500 INTERNAL SERVER ERROR:
                - Generic error.
        """
        # Parse and validate request body
        try:
            body: dict = FriendRequestRespondValidator().load(request.get_json())
            sender_netid = body["sender_netid"]
            recipient_netid = body["recipient_netid"]
            accept: bool = body["accept"]
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST
        
        #Query Database
        try:
            
            if not self.user_network.get_user(sender_netid):
                raise UserNotFoundException(sender_netid)
            if not self.user_network.get_user(recipient_netid):
                raise UserNotFoundException(recipient_netid)
            
            if not self.user_network.check_friend_request(sender_netid, recipient_netid):
                raise NoFriendRequestException(sender_netid, recipient_netid)

            if accept: 
                self.user_network.connect_users(sender_netid, recipient_netid)
                message = "Accepted friend request successfully"
            else: 
                self.user_network.remove_friend_request(sender_netid, recipient_netid)
                message = "Rejected friend request successfully"
        # Return response
        except NoInputsException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except UserNotFoundException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except NotFriendsException as e: 
            return e.msg, status.HTTP_400_BAD_REQUEST
        except Exception as e:
            self.logger.log(ERROR, str(e))
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        return message, status.HTTP_200_OK
 