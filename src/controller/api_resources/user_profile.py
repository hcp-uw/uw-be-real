# Flask imports
from flask import Flask
from flask_api import status
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

# Validation and Loggingimport
from logging import Logger
from cerberus import Validator
from src.model.schemas.user_schema import USER_PROFILE_SCHEMA as SCHEMA

# Controller imports
from src.controller.exceptions.user_exceptions import UserNotFoundException
from src.controller.exceptions.generic_exceptions import NoInputsException


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

    @staticmethod
    def _get_request_parser() -> tuple[dict, dict]:
        """Parses the GET request body and returns a tuple of
        request payload data (dict) and error messages (dict).
        """
        # Setup body argument parser
        parse: RequestParser = RequestParser(bundle_errors=True)
        parse.add_argument(
            "netid",
            required=True,
            type=str,
            help=SCHEMA_ERROR["netid"],
        )
        # Parse body arguments
        try:
            body = parse.parse_args(strict=True)
        # 400 Bad Request on extra parameters
        except Exception as e:
            return {}, PROPERTY_ERROR

        # Validate arguments
        validator: Validator = Validator()
        validator.validate(body, SCHEMA)

        # Build error message
        error_msg: dict = {arg: SCHEMA_ERROR[arg] for arg in validator.errors}

        return body, error_msg
<<<<<<< Updated upstream

    def get(self):
=======
    
    def get(self, netid):
>>>>>>> Stashed changes
        """Get user information from the provided information in the request payload.

        Args:
            netid (str): The UW NetID of the user.

        Returns:
            Serialized JSON data of the user.

        Responses:
            200 OK:
                - User successfully retrieved.
            400 BAD REQUEST:
                - Invalid request payload, no changes made.
            500 INTERNAL SERVER ERROR:
                - Generic error.
        """
<<<<<<< Updated upstream
        body, validator_errors = self._get_request_parser()
        if validator_errors:
            return validator_errors, status.HTTP_400_BAD_REQUEST

        netid: str = body["netid"]
=======
        # body, validator_errors = self._get_request_parser()
        # if validator_errors:
        #     return validator_errors, status.HTTP_400_BAD_REQUEST
        
        # netid: str = body["netid"]
        # validator: Validator = Validator()
        # validator.validate(netid, SCHEMA)
        # validator_errors: dict = {arg: SCHEMA_ERROR[arg] for arg in validator.errors}
        # if validator_errors:
        #     return validator_errors, status.HTTP_400_BAD_REQUEST
>>>>>>> Stashed changes

        # Query Database
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
<<<<<<< Updated upstream
=======
    
>>>>>>> Stashed changes
