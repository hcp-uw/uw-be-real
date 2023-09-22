# Flask imports
from flask import request
from flask_api import status
from flask_restful import Resource

# Logging and validation import 
from logging import Logger
from marshmallow import ValidationError
from controller.exceptions.friend_exceptions import FriendsAlreadyException

# Controller imports
from controller.exceptions.generic_exceptions import NoInputsException
from controller.exceptions.user_exceptions import UserNotFoundException
from controller.validations.friend_request_send_validator import FriendRequestSendValidator

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.data_access.user_network import UserNetwork

class FriendRequestSend(Resource):
    def __init__(self, user_network: UserNetwork, logger: Logger) -> None:
        """Instantiates a FriendRequestSend API Resource for a user to send a friend request to another user.

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
        """Get user's friends information from the provided information in the request payload.

        Args:
            sender_netid (str): The UW NetID of the user sending the friend request 
            recipient_netid (str): The UW NetID of the user receiving the friend request


        Responses:
            200 OK:
                - Successfully sent a friend request from sender_netid to recipient_netid
            400 BAD REQUEST:
                - Invalid request, no changes made.
            409 CONFLICT: 
                - Users are already friends.
            500 INTERNAL SERVER ERROR:
                - Generic error.
        """
        # Parse and validate request body
        try:
            body: dict = FriendRequestSendValidator().load(request.args)
            sender_netid = body["sender_netid"]
            recipient_netid = body["recipient_netid"]
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST
        
        #Query Database
        try:
            
            if not self.user_network.get_user(sender_netid):
                raise UserNotFoundException(sender_netid)
            if not self.user_network.get_user(recipient_netid):
                raise UserNotFoundException(recipient_netid)
            
            if self.user_network.check_friend(sender_netid, recipient_netid):
                raise FriendsAlreadyException(sender_netid, recipient_netid)
            if self.user_network.check_friend_request(recipient_netid, sender_netid):
                self.user_network.connect_users(sender_netid, recipient_netid)
                message = "Recipient sent friend request, now connected as mutuals"
            else: 
                self.user_network.send_friend_request(sender_netid, recipient_netid)
                message = "Recipient has now received friend request"
        
        # Return response
        except NoInputsException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except UserNotFoundException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except FriendsAlreadyException as e: 
            return e.msg, status.HTTP_409_BAD_REQUEST
        except Exception as e:
            self.logger.log(ERROR, str(e))
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        return message, status.HTTP_200_OK
 