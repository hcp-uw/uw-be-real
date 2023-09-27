# Flask imports
from flask import request
from flask_api import status
from flask_restful import Resource

# Logging and validation import 
from logging import Logger
from marshmallow import ValidationError

# Controller imports
from controller.exceptions.generic_exceptions import NoInputsException
from controller.validations.user_search_validator import UserSearchValidator

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.data_access.user_network import UserNetwork

class UserSearch(Resource):
    def __init__(self, user_network: UserNetwork, logger: Logger) -> None:
        """Instantiates a UserSearch API Resource for searching users whose 
        usernames start with the supplied string

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
        """Get users whose usernames start with provided string in the request payload.

        Args:
            search_str (str): The search term to be matched to usernames.
            netid (str): The netid of the current user whose blocked users
              will not appear in the search (not required).


        Returns:
            Serialized JSON data of the user's friends.

        Responses:
            200 OK:
                - A list of users whose names start with search_str, excluding
                those blocked by netid
            400 BAD REQUEST:
                - Invalid request, no changes made.
            500 INTERNAL SERVER ERROR:
                - Generic error.
        """
        # Parse and validate request body
        try:
            body: dict = UserSearchValidator().load(request.args)
            search_str = body["search_str"]
            netid = body["netid"]
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST
        
        #Query Database        
        try:
            user_info: list[str] = self.user_network.search_users(netid, search_str)


        # Return response
        except NoInputsException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except Exception as e:
            self.logger.log(ERROR, str(e))
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        return user_info, status.HTTP_200_OK
 