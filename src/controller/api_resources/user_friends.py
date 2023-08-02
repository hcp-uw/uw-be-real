# Flask imports
from flask import request
from flask_api import status
from flask_restful import Resource

# Logging and validation import 
from logging import Logger
from marshmallow import ValidationError

# Controller imports
from src.controller.exceptions.neo4j_exceptions import QueryFailureException
from src.controller.exceptions.user_exceptions import *
from src.controller.exceptions.generic_exceptions import NoInputsException
from src.controller.validations.user_friends_validator import *

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.data_access.user_network import UserNetwork

class UserFriends(Resource):
    def __init__(self, user_network: UserNetwork, logger: Logger) -> None:
        """Instantiates a UserFriends API Resource for retrieving and updating user friends.

        Methods:
            - GET
            - PUT

        Args:
            user_network (UserNetwork): A valid UserNetwork.

        Returns:
            None.
        """
        self.logger: Logger = logger
        self.user_network: UserNetwork = user_network

    def put(self):
        """ Updates or adds user's friends from the provided information in the request payload.

        Args:
            sender_netid (str): The first UW NetID pertaining to the first user.

            connection (str): The connection between the two users (request, accept, reject, or unfriend)

            recipient_netid (str): The second UW NetID pertaining to the second user who
                                the first user wants to request/accept/reject/unfriend.

        Responses:
            200 OK:
                - User information successfully updated.
            
            400 BAD REQUEST:
                - Invalid request payload, no changes made.

            500 INTERNAL SERVER ERROR:
                - Failed to excute query.
                - Generic error.
        """
        try:
            body: dict = UserFriendsPutValidator().load(request.get_json())
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST
        sender_netid: str = body["sender_netid"]
        connection: str = body["connection"]
        recipient_netid: str = body["recipient_netid"]

        # Query database
        try:
            self.user_network.friend_request(
                sender_netid=sender_netid,
                connection=connection,
                recipient_netid=recipient_netid,
            )

        # Return response
        except NoInputsException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except ExistingConnectionException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except InvalidConnectionException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except QueryFailureException as e:
            self.logger.log(ERROR, e.msg)
            return QUERY_FAILED_TO_EXECUTE, status.HTTP_500_INTERNAL_SERVER_ERROR

        except Exception as e:
            self.logger.log(ERROR, str(e))
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        return status.HTTP_200_OK
    