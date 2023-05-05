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

    def post(self):
        # Parse request body
        parse: RequestParser = RequestParser()
        parse.add_argument(
            "netid",
            required=True,
            type=str,
        )
        parse.add_argument(
            "email",
            required=True,
            type=str,
        )
        parse.add_argument(
            "username",
            required=True,
            type=str,
        )
        parse.add_argument(
            "fullname",
            required=True,
            type=str,
        )
        args: dict = parse.parse_args()

        # Validate arguments
        validator: Validator = Validator()
        validator.validate(args, CREATE_USER_SCHEMA)

        # 400 Bad request
        if validator.errors:
            return validator.errors, status.HTTP_400_BAD_REQUEST

        self.user_network.create_user(
            username=args["username"],
            fullname=args["fullname"],
            netid=args["netid"],
            email=args["email"],
        )
        return status.HTTP_200_OK
