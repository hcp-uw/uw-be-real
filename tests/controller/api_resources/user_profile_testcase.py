# Flask imports
from flask_api import status

# Unit testing tool imports
import requests
import unittest

# Model imports
from src.model.data_access.user_network import UserNetwork

# Config import
from tests import config


class UserProfileTestCase(unittest.TestCase):
    """UserProfile Unit test module."""

    def setUp(self) -> None:
        """"""
        self.user_network: UserNetwork = config.USER_NETWORK
        self.url_user_create: str = f"{config.BASE_URL}/api/user-create"
        self.url_user_profile: str = f"{config.BASE_URL}/api/user-profile"

    def test_valid_request_should_return_200(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        data_user_create = {
            "username": "testuser1",
            "firstname": "user1",
            "lastname": "test",
            "email": "testuser1@uw.edu",
        }

        data_user_profile = {
            "netid": "testuser1",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        response_user_create = requests.post(self.url_user_create, json=data_user_create, headers=headers)
        response_user_profile = requests.get(self.url_user_profile, json=data_user_profile, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = response_user_create.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_create.text}",
        )

        received: str = response_user_profile.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_profile.text}",
        )