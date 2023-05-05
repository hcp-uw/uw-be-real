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
    def _post_request_parser() -> dict:
        # Setup body argument parser
        parse: RequestParser = RequestParser(bundle_errors=True)
        parse.add_argument(
            "netid",
            required=True,
            type=str,
            help=SCHEMA["netid"],
        )
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
        # Parse request body
        body, validator_errors = self._post_request_parser()

        # 400 Bad request on invalid request
        if validator_errors:
            return validator_errors, status.HTTP_400_BAD_REQUEST

        try:
            self.user_network.create_user(
                username=body["username"],
                fullname=body["fullname"],
                netid=body["netid"],
                email=body["email"],
            )

        except NoInputsException as e:
            return e.msg, status.HTTP_400_BAD_REQUEST

        except UserAlreadyExistsException as e:
            return e.msg, status.HTTP_500_INTERNAL_SERVER_ERROR

        except QueryFailureException as e:
            self.logger.log(ERROR, e.msg)
            return QUERY_FAILED_TO_EXECUTE, status.HTTP_500_INTERNAL_SERVER_ERROR

        except Exception as e:
            self.logger.log(ERROR, e.msg)
            return GENERIC_INTERNAL_SERVER_ERROR, status.HTTP_500_INTERNAL_SERVER_ERROR

        return USER_CREATE_SUCCESS, status.HTTP_201_CREATED
