# Flask imports
from flask_api import status

# Unit testing tool imports
import requests
import unittest

# Model imports
from src.model.data_access.user_network import UserNetwork
from src.model.queries.neo4j_queries import delete_database


class UserCreateTest(unittest.TestCase):
    """UserRoute Unit test module."""

    def __init__(self, user_network: UserNetwork, base_url: str) -> None:
        """"""
        super().__init__()
        self.user_network: UserNetwork = user_network
        self.url: str = f"{base_url}/api/user-create"

    def _delete_all_users(self) -> None:
        """Deletes all users from the network."""
        self.user_network._database_query(delete_database())

    def valid_request_should_return_201_created_test(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clean database
        self._delete_all_users()

        # Request payload
        data = {
            "username": "testuser1",
            "fullname": "user1,test",
            "email": "testuser1@uw.edu",
        }

        # Request header
        headers = {"content-type": "application/json"}

        ### ACT: Perform action to invoke API.
        response = requests.post(self.url, data=data, headers=headers)

        ### ASSERT: Verify expected outcome.
        assert response.status_code == status.HTTP_201_CREATED
