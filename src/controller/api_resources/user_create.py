# Flask imports
from flask_api import status
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

# Validation import
from cerberus import Validator
from src.model.schemas.user_schema import CREATE_USER_SCHEMA

# Api util imports
from src.model.data_access.user_content import UserContent
from src.model.data_access.user_network import UserNetwork


class UserCreate(Resource):
    def __init__(self, user_network: UserNetwork) -> None:
        """Instantiates a UserCreate API Resource for creating new user accounts.

        Methods:
            - POST

        Args:
            user_network (UserNetwork): A valid UserNetwork.

        Returns:
            None.
        """
        self.user_network: UserNetwork = user_network

    @staticmethod
    def _post_request_parser() -> dict:
        parse: RequestParser = RequestParser(bundle_errors=True)
        parse.add_argument(
            "netid",
            required=True,
            type=str,
            help="netid must be a non-empty string.",
        )
        parse.add_argument(
            "email",
            required=True,
            type=str,
            help="email must be a non-empty string and have a @uw.edu domain name.",
        )
        parse.add_argument(
            "username",
            required=True,
            type=str,
            help="username must be a non-empty string within 64 characters.",
        )
        parse.add_argument(
            "fullname",
            required=True,
            type=str,
            help="fullname must be a non-empty comma-separated string (last,first) where both names must be within 64 characters.",
        )
        return parse.parse_args()

    def post(self):
        # Parse request body
        body = self._post_request_parser()

        # Validate arguments
        validator: Validator = Validator()
        validator.validate(body, CREATE_USER_SCHEMA)

        # 400 Bad request on invalid request
        if validator.errors:
            return validator.errors, status.HTTP_400_BAD_REQUEST

        return status.HTTP_200_OK

        self.user_network.create_user(
            username=body["username"],
            fullname=body["fullname"],
            netid=body["netid"],
            email=body["email"],
        )
