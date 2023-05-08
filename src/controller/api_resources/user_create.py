# Flask imports
from flask_api import status
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

# Validation and Loggingimport
from logging import Logger
from cerberus import Validator
from src.model.schemas.user_schema import (
    CREATE_USER_SCHEMA as SCHEMA,
    CREATE_USER_SCHEMA_ERROR_MSG as SCHEMA_ERROR,
)

# Controller imports
from src.controller.exceptions.neo4j_exceptions import (
    UserAlreadyExistsException,
    QueryFailureException,
)
from src.controller.exceptions.generic_exceptions import NoInputsException

# Model imports
from src.model.constants.http_response_messages import *
from src.model.constants.logger_constants import *
from src.model.data_access.user_network import UserNetwork


class UserCreate(Resource):
    def __init__(self, user_network: UserNetwork, logger: Logger) -> None:
        """Instantiates a UserCreate API Resource for creating new user accounts.

        Methods:
            - POST

        Args:
            user_network (UserNetwork): A valid UserNetwork.

        Returns:
            None.
        """
        self.logger: Logger = logger
        self.user_network: UserNetwork = user_network

    @staticmethod
    def _post_request_parser() -> tuple[dict, dict]:
        """Parses the POST request body and returns a tuple of
        request payload data (dict) and error messages (dict).
        """
        # Setup body argument parser
        parse: RequestParser = RequestParser(bundle_errors=True)
        parse.add_argument(
            "email",
            required=True,
            type=str,
            help=SCHEMA["email"],
        )
        parse.add_argument(
            "username",
            required=True,
            type=str,
            help=SCHEMA["username"],
        )
        parse.add_argument(
            "fullname",
            required=True,
            type=str,
            help=SCHEMA["fullname"],
        )
        # Parse body arguments
        body = parse.parse_args()

        # Validate arguments
        validator: Validator = Validator()
        validator.validate(body, SCHEMA)

        # Build error message
        error_msg: dict = {arg: SCHEMA_ERROR[arg] for arg in validator.errors}

        return body, error_msg

    def post(self):
        """Creates a new user from the provided user information in the request payload.

        Args:
            username (str): A username between 1-64 characters (inclusive).
            fullname (str): A comma separated last,first name. Each name is between 1-64 characters (inclusive).
            email (str): A [unique] UW email of the new user.

        Responses:
            201 CREATED:
                - New user successfully created.
            400 BAD REQUEST:
                - Invalid request payload, no changes made.
            409 CONFLICT:
                - A user account already exists under the provided credentials.
            500 INTERNAL SERVER ERROR:
                - Failed to excute query.
                - Generic error.
        """
        # Parse and validate request body
        body, validator_errors = self._post_request_parser()
        if validator_errors:
            return validator_errors, status.HTTP_400_BAD_REQUEST

        # String parse to get NetID from UW email.
        email: str = body["email"]
        netid: str = email.split("@")[0]

        # Query database
        try:
            self.user_network.create_user(
                username=body["username"],
                fullname=body["fullname"],
                netid=netid,
                email=email,
            )

        # Return response
        except NoInputsException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST

        except UserAlreadyExistsException as e:
            return e.msg, status.HTTP_409_CONFLICT

        except QueryFailureException as e:
            self.logger.log(ERROR, e.msg)
            return QUERY_FAILED_TO_EXECUTE, status.HTTP_500_INTERNAL_SERVER_ERROR

        except Exception as e:
            self.logger.log(ERROR, str(e))
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        return USER_CREATE_SUCCESS, status.HTTP_201_CREATED
