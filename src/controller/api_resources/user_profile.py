# Flask imports
from flask import request
from flask_api import status
from flask_restful import Resource

# Logging and validation import 
from logging import Logger
from marshmallow import ValidationError

# Controller imports
from src.controller.exceptions.neo4j_exceptions import QueryFailureException
from src.controller.exceptions.user_exceptions import UserNotFoundException
from src.controller.exceptions.generic_exceptions import NoInputsException
from src.controller.validations.user_profile_validator import *

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.data_access.user_network import UserNetwork

class UserProfile(Resource):
    def __init__(self, user_network: UserNetwork, logger: Logger) -> None:
        """Instantiates a UserProfile API Resource for retrieving and updating user information.

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
    
    def get(self):
        """Get user information from the provided information in the request payload.

        Args:
            netid (str): The UW NetID of the user.

        Returns:
            Serialized JSON data of the user.

        Responses:
            200 OK:
                - User successfully retrieved.

            400 BAD REQUEST:
                - Invalid request, no changes made.

            500 INTERNAL SERVER ERROR:
                - Generic error.
        """
        # Parse and validate request body
        try:
            body: dict = UserProfileGetValidator().load(request.args)
            netid = body["netid"]
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST
        
        #Query Database        
        try:
            user_info: dict = self.user_network.get_user(netid)
            if not user_info:
               raise UserNotFoundException(netid) 
        
        # Return response
        except NoInputsException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except UserNotFoundException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except Exception as e:
            self.logger.log(ERROR, str(e))
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        return user_info, status.HTTP_200_OK
    
    def put(self):
        """ Updates or adds user information from the provided information in the request payload.

        Args:
            netid (str): The UW NetID of the user.
        
            username (str, optional): A username between 1-64 characters (inclusive).

            firstname (str, optional): A first name between 1-64 characters (inclusive).

            lastname (str, optional): A last name between 1-64 characters (inclusive).

            profile-image (URL, optional): A URL of a picture for the user's profile-image.

            friends (list, optional): A list of a user's friends.

            phone (str, optional): A phone number with 10 digits.

            birthdate (datetime, optional): A birthdate corresponding to the user.

            campus (string, optional): The campus where the user attends.

            major (string, optional): The user's major.

            interests (list, optional): Interests that a user has.

        Responses:
            200 OK:
                - User information successfully updated.
            
            400 BAD REQUEST:
                - Invalid request payload, no changes made.

            500 INTERNAL SERVER ERROR:
                - Failed to excute query.
                - Generic error.
        """
        # Parse and validate request body
        try:
            body: dict = UserProfilePutValidator().load(request.get_json())
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST
        netid = body["netid"]
        del body["netid"]

        # Query database
        try:
            self.user_network.update_user(
                netid=netid,
                **body
            )

        # Return response
        except NoInputsException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST
        
        except QueryFailureException as e:
            self.logger.log(ERROR, e.msg)
            return QUERY_FAILED_TO_EXECUTE, status.HTTP_500_INTERNAL_SERVER_ERROR

        except Exception as e:
            self.logger.log(ERROR, str(e))
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        return status.HTTP_200_OK
    