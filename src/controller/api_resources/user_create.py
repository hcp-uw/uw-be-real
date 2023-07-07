# Flask imports
from flask import request
from flask_api import status
from flask_restful import Resource

# Logging and validation import
from logging import Logger
from marshmallow import ValidationError

# Controller imports
from src.controller.exceptions.neo4j_exceptions import (
    UserAlreadyExistsException,
    QueryFailureException,
)
from src.controller.exceptions.generic_exceptions import NoInputsException
from src.controller.validations.user_create_validator import UserCreateValidator

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

    def post(self):
        """Creates a new user from the provided user information in the request payload.

        Args:
            username (str): A username between 1-64 characters (inclusive).
            firstname (str): A first name between 1-64 characters (inclusive).
            lastname (str): A last name between 1-64 characters (inclusive).
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
        try:
            body: dict = UserCreateValidator().load(request.get_json())

            # String parse to get NetID from UW email.
            email: str = body["email"]
            netid: str = email.split("@")[0]

            # Query database
            self.user_network.create_user(
                username=body["username"],
                firstname=body["firstname"],
                lastname=body["lastname"],
                netid=netid,
                email=email,
            )

        # Return response
        except ValidationError as e:
            return e.messages, status.HTTP_400_BAD_REQUEST

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
