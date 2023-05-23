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


    # GET REQUESTS
    def test_get_valid_user_request_should_return_200(self) -> None:
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

        self.url_user_profile: str = f"{config.BASE_URL}/api/user-profile?netid=testuser1"

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

    def test_get_invalid_user_request_should_return_400(self) -> None:
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

        self.url_user_profile: str = f"{config.BASE_URL}/api/user-profile?netid=testuser2"

        data_user_profile_invalid = {
            "netid": "testuser2",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        response_user_create = requests.post(self.url_user_create, json=data_user_create, headers=headers)
        response_user_profile_invalid = requests.get(self.url_user_profile, json=data_user_profile_invalid, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = response_user_create.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_create.text}",
        )

        received: str = response_user_profile_invalid.status_code
        expected: str = status.HTTP_400_BAD_REQUEST
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_profile_invalid.text}",
        )

    def test_get_empty_user_request_should_return_400(self) -> None:
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

        self.url_user_profile: str = f"{config.BASE_URL}/api/user-profile?netid="

        data_user_profile_empty = {
            "netid": "",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        response_user_create = requests.post(self.url_user_create, json=data_user_create, headers=headers)
        response_user_profile_empty = requests.get(self.url_user_profile, json=data_user_profile_empty, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = response_user_create.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_create.text}",
        )

        received: str = response_user_profile_empty.status_code
        expected: str = status.HTTP_400_BAD_REQUEST
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_profile_empty.text}",
        )

    
    # PUT REQUESTS
    def test_put_valid_campus_should_return_200(self) -> None:
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

        data_user_profile_campus = {
            "netid": "testuser1",
            "campus": "seattle",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        response_user_create = requests.post(self.url_user_create, json=data_user_create, headers=headers)
        response_user_profile_campus = requests.put(self.url_user_profile, json=data_user_profile_campus, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = response_user_create.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_create.text}",
        )

        received: str = response_user_profile_campus.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_profile_campus.text}",
        )

    def test_put_multiple_new_valid_data_should_return_200(self) -> None:
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
            "campus": "seattle",
            "phone": "1234567890",
            "interests": ["basketball", "soccer", "football"],
            "birthdate": "2000-01-01",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        response_user_create = requests.post(self.url_user_create, json=data_user_create, headers=headers)
        response_user_profile = requests.put(self.url_user_profile, json=data_user_profile, headers=headers)

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

    def test_put_multiple_new_invalid_data_should_return_400(self) -> None:
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
            "campus": "vancouver",
            "phone": "abc",
            "interests": ["basketball", "soccer", "football"],
            "birthdate": "05-21-2023",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        response_user_create = requests.post(self.url_user_create, json=data_user_create, headers=headers)
        response_user_profile = requests.put(self.url_user_profile, json=data_user_profile, headers=headers)

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
        expected: str = status.HTTP_400_BAD_REQUEST
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_profile.text}",
        )

    def test_put_multiple_new_invalid_fields_should_return_400(self) -> None:
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
            "address": "1410 NE Campus Parkway Seattle, WA 98195",
            "birthday": "2000-01-01",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        response_user_create = requests.post(self.url_user_create, json=data_user_create, headers=headers)
        response_user_profile = requests.put(self.url_user_profile, json=data_user_profile, headers=headers)

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
        expected: str = status.HTTP_400_BAD_REQUEST
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_profile.text}",
        )

    def test_put_multiple_optional_empty_data_should_return_200(self) -> None:
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
            "campus": "seattle",
            "phone": "1234567890",
            "interests": ["basketball", "soccer", "football"],
            "birthdate": "2000-01-01",
        }

        data_user_empty = {
            "netid": "testuser1",
            "campus": "",
            "phone": "",
            "interests": [],
            "birthdate": "",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        response_user_create = requests.post(self.url_user_create, json=data_user_create, headers=headers)
        response_user_profile = requests.put(self.url_user_profile, json=data_user_profile, headers=headers)
        response_user_empty = requests.put(self.url_user_profile, json=data_user_empty, headers=headers)

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

        received: str = response_user_empty.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_empty.text}",
        )

    def test_put_multiple_required_non_empty_data_as_empty_should_return_400(self) -> None:
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

        data_user_empty = {
            "netid": "testuser1",
            "firstname": "",
            "lastname": "",
            "username": "",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        response_user_create = requests.post(self.url_user_create, json=data_user_create, headers=headers)
        response_user_empty = requests.put(self.url_user_profile, json=data_user_empty, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = response_user_create.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_create.text}",
        )

        received: str = response_user_empty.status_code
        expected: str = status.HTTP_400_BAD_REQUEST
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response_user_empty.text}",
        )