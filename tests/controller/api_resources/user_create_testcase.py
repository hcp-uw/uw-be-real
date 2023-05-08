# Flask imports
from flask_api import status

# Unit testing tool imports
import requests
import unittest

# Model imports
from src.model.data_access.user_network import UserNetwork

# Config import
from tests import config


class UserCreateTestCase(unittest.TestCase):
    """UserRoute Unit test module."""

    def setUp(self) -> None:
        """"""
        self.user_network: UserNetwork = config.USER_NETWORK
        self.url: str = f"{config.BASE_URL}/api/user-create"

    def test_valid_request_should_return_201(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        data = {
            "username": "testuser1",
            "fullname": "user1,test",
            "email": "testuser1@uw.edu",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        response = requests.post(self.url, json=data, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = response.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response.text}",
        )

    def test_invalid_request_should_return_400(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload - Invalid character(space) in username and fullname, and invalid email domain name.
        data = {
            "username": "test user1",
            "fullname": "user1, test",
            "email": "testuser1@uwww.edu",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        response = requests.post(self.url, json=data, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = response.status_code
        expected: str = status.HTTP_400_BAD_REQUEST
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response.text}",
        )
