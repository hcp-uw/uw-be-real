# Flask imports
from flask_api import status

# Unit testing tool imports
import requests
import unittest

# Model imports
from src.model.data_access.user_network import UserNetwork

# Config import
from tests import config


class UserFriendsTestCase(unittest.TestCase):
    """UserFriends Unit test module."""

    def setUp(self) -> None:
        """"""
        self.user_network: UserNetwork = config.USER_NETWORK
        self.url_user_create: str = f"{config.BASE_URL}/api/user-create"
        self.url_user_friends: str = f"{config.BASE_URL}/api/user-friends"

    def test_valid_request_should_return_200(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        user1 = {
            "username": "user1",
            "firstname": "user1",
            "lastname": "user1",
            "email": "user1@uw.edu",
        }

        user2 = {
            "username": "user2",
            "firstname": "user2",
            "lastname": "user2",
            "email": "user2@uw.edu",
        }

        request = {
            "sender_netid": "user1",
            "connection": "request",
            "recipient_netid": "user2",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        create_user1 = requests.post(self.url_user_create, json=user1, headers=headers)
        create_user2 = requests.post(self.url_user_create, json=user2, headers=headers)
        response = requests.put(self.url_user_friends, json=request, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = create_user1.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user1.text}",
        )

        received: str = create_user2.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user2.text}",
        )

        received: str = response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response.text}",
        )

    def test_request_then_decline_should_return_200(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        user1 = {
            "username": "user1",
            "firstname": "user1",
            "lastname": "user1",
            "email": "user1@uw.edu",
        }

        user2 = {
            "username": "user2",
            "firstname": "user2",
            "lastname": "user2",
            "email": "user2@uw.edu",
        }

        request = {
            "sender_netid": "user1",
            "connection": "request",
            "recipient_netid": "user2",
        }

        decline = {
            "sender_netid": "user2",
            "connection": "decline",
            "recipient_netid": "user1",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        create_user1 = requests.post(self.url_user_create, json=user1, headers=headers)
        create_user2 = requests.post(self.url_user_create, json=user2, headers=headers)
        request_response = requests.put(self.url_user_friends, json=request, headers=headers)
        decline_response = requests.put(self.url_user_friends, json=decline, headers=headers)
        

        ### ASSERT: Verify expected outcome.
        received: str = create_user1.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user1.text}",
        )

        received: str = create_user2.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user2.text}",
        )

        received: str = request_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{request_response.text}",
        )

        received: str = decline_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{decline_response.text}",
        )

    def test_request_then_accept_should_return_200(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        user1 = {
            "username": "user1",
            "firstname": "user1",
            "lastname": "user1",
            "email": "user1@uw.edu",
        }

        user2 = {
            "username": "user2",
            "firstname": "user2",
            "lastname": "user2",
            "email": "user2@uw.edu",
        }

        request = {
            "sender_netid": "user1",
            "connection": "request",
            "recipient_netid": "user2",
        }

        accept = {
            "sender_netid": "user2",
            "connection": "accept",
            "recipient_netid": "user1",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        create_user1 = requests.post(self.url_user_create, json=user1, headers=headers)
        create_user2 = requests.post(self.url_user_create, json=user2, headers=headers)
        request_response = requests.put(self.url_user_friends, json=request, headers=headers)
        accept_response = requests.put(self.url_user_friends, json=accept, headers=headers)
        

        ### ASSERT: Verify expected outcome.
        received: str = create_user1.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user1.text}",
        )

        received: str = create_user2.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user2.text}",
        )

        received: str = request_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{request_response.text}",
        )

        received: str = accept_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{accept_response.text}",
        )

    def test_request_then_accet_then_unfriend_should_return_200(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        user1 = {
            "username": "user1",
            "firstname": "user1",
            "lastname": "user1",
            "email": "user1@uw.edu",
        }

        user2 = {
            "username": "user2",
            "firstname": "user2",
            "lastname": "user2",
            "email": "user2@uw.edu",
        }

        request = {
            "sender_netid": "user1",
            "connection": "request",
            "recipient_netid": "user2",
        }

        accept = {
            "sender_netid": "user2",
            "connection": "accept",
            "recipient_netid": "user1",
        }

        unfriend = {
            "sender_netid": "user1",
            "connection": "unfriend",
            "recipient_netid": "user2",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        create_user1 = requests.post(self.url_user_create, json=user1, headers=headers)
        create_user2 = requests.post(self.url_user_create, json=user2, headers=headers)
        request_response = requests.put(self.url_user_friends, json=request, headers=headers)
        accept_response = requests.put(self.url_user_friends, json=accept, headers=headers)
        unfriend_response = requests.put(self.url_user_friends, json=unfriend, headers=headers)
        

        ### ASSERT: Verify expected outcome.
        received: str = create_user1.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user1.text}",
        )

        received: str = create_user2.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user2.text}",
        )

        received: str = request_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{request_response.text}",
        )

        received: str = accept_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{accept_response.text}",
        )

        received: str = unfriend_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{unfriend_response.text}",
        )

    def test_request_then_request_should_return_400(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        user1 = {
            "username": "user1",
            "firstname": "user1",
            "lastname": "user1",
            "email": "user1@uw.edu",
        }

        user2 = {
            "username": "user2",
            "firstname": "user2",
            "lastname": "user2",
            "email": "user2@uw.edu",
        }

        request = {
            "sender_netid": "user1",
            "connection": "request",
            "recipient_netid": "user2",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        create_user1 = requests.post(self.url_user_create, json=user1, headers=headers)
        create_user2 = requests.post(self.url_user_create, json=user2, headers=headers)
        request1_response = requests.put(self.url_user_friends, json=request, headers=headers)
        request2_response = requests.put(self.url_user_friends, json=request, headers=headers)
        

        ### ASSERT: Verify expected outcome.
        received: str = create_user1.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user1.text}",
        )

        received: str = create_user2.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user2.text}",
        )

        received: str = request1_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{request1_response.text}",
        )

        received: str = request2_response.status_code
        expected: str = status.HTTP_400_BAD_REQUEST
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{request2_response.text}",
        )

    def test_request_then_decline_then_decline_should_return_400(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        user1 = {
            "username": "user1",
            "firstname": "user1",
            "lastname": "user1",
            "email": "user1@uw.edu",
        }

        user2 = {
            "username": "user2",
            "firstname": "user2",
            "lastname": "user2",
            "email": "user2@uw.edu",
        }

        request = {
            "sender_netid": "user1",
            "connection": "request",
            "recipient_netid": "user2",
        }

        decline = {
            "sender_netid": "user2",
            "connection": "decline",
            "recipient_netid": "user1",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        create_user1 = requests.post(self.url_user_create, json=user1, headers=headers)
        create_user2 = requests.post(self.url_user_create, json=user2, headers=headers)
        request_response = requests.put(self.url_user_friends, json=request, headers=headers)
        decline1_response = requests.put(self.url_user_friends, json=decline, headers=headers)
        decline2_response = requests.put(self.url_user_friends, json=decline, headers=headers)
        

        ### ASSERT: Verify expected outcome.
        received: str = create_user1.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user1.text}",
        )

        received: str = create_user2.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user2.text}",
        )

        received: str = request_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{request_response.text}",
        )

        received: str = decline1_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{decline1_response.text}",
        )

        received: str = decline2_response.status_code
        expected: str = status.HTTP_400_BAD_REQUEST
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{decline2_response.text}",
        )

    def test_unfriend_with_no_friend_should_return_400(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        user1 = {
            "username": "user1",
            "firstname": "user1",
            "lastname": "user1",
            "email": "user1@uw.edu",
        }

        user2 = {
            "username": "user2",
            "firstname": "user2",
            "lastname": "user2",
            "email": "user2@uw.edu",
        }

        unfriend = {
            "sender_netid": "user1",
            "connection": "unfriend",
            "recipient_netid": "user2",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        create_user1 = requests.post(self.url_user_create, json=user1, headers=headers)
        create_user2 = requests.post(self.url_user_create, json=user2, headers=headers)
        response = requests.put(self.url_user_friends, json=unfriend, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = create_user1.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user1.text}",
        )

        received: str = create_user2.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user2.text}",
        )

        received: str = response.status_code
        expected: str = status.HTTP_400_BAD_REQUEST
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response.text}",
        )

    def test_blocked_should_return_200(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        user1 = {
            "username": "user1",
            "firstname": "user1",
            "lastname": "user1",
            "email": "user1@uw.edu",
        }

        user2 = {
            "username": "user2",
            "firstname": "user2",
            "lastname": "user2",
            "email": "user2@uw.edu",
        }

        request = {
            "sender_netid": "user1",
            "connection": "block",
            "recipient_netid": "user2",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        create_user1 = requests.post(self.url_user_create, json=user1, headers=headers)
        create_user2 = requests.post(self.url_user_create, json=user2, headers=headers)
        response = requests.put(self.url_user_friends, json=request, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = create_user1.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user1.text}",
        )

        received: str = create_user2.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user2.text}",
        )

        received: str = response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{response.text}",
        )

    def test_block_then_unblock_should_return_200(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        user1 = {
            "username": "user1",
            "firstname": "user1",
            "lastname": "user1",
            "email": "user1@uw.edu",
        }

        user2 = {
            "username": "user2",
            "firstname": "user2",
            "lastname": "user2",
            "email": "user2@uw.edu",
        }

        block = {
            "sender_netid": "user1",
            "connection": "block",
            "recipient_netid": "user2",
        }

        unblock = {
            "sender_netid": "user1",
            "connection": "unblock",
            "recipient_netid": "user2",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        create_user1 = requests.post(self.url_user_create, json=user1, headers=headers)
        create_user2 = requests.post(self.url_user_create, json=user2, headers=headers)
        block_response = requests.put(self.url_user_friends, json=block, headers=headers)
        unblock_response = requests.put(self.url_user_friends, json=unblock, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = create_user1.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user1.text}",
        )

        received: str = create_user2.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user2.text}",
        )

        received: str = block_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{block_response.text}",
        )

        received: str = unblock_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{unblock_response.text}",
        )

    def test_block_then_request_should_return_400(self) -> None:
        ### ARRANGE: Set up necessary preconditions.
        # Clear all data in database
        config.clear_database()

        # Request payload
        user1 = {
            "username": "user1",
            "firstname": "user1",
            "lastname": "user1",
            "email": "user1@uw.edu",
        }

        user2 = {
            "username": "user2",
            "firstname": "user2",
            "lastname": "user2",
            "email": "user2@uw.edu",
        }

        block = {
            "sender_netid": "user1",
            "connection": "block",
            "recipient_netid": "user2",
        }

        request = {
            "sender_netid": "user2",
            "connection": "request",
            "recipient_netid": "user1",
        }

        # Request header
        headers = {
            "content-type": "application/json",
        }

        ### ACT: Perform action to invoke API.
        create_user1 = requests.post(self.url_user_create, json=user1, headers=headers)
        create_user2 = requests.post(self.url_user_create, json=user2, headers=headers)
        block_response = requests.put(self.url_user_friends, json=block, headers=headers)
        request_response = requests.put(self.url_user_friends, json=request, headers=headers)

        ### ASSERT: Verify expected outcome.
        received: str = create_user1.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user1.text}",
        )

        received: str = create_user2.status_code
        expected: str = status.HTTP_201_CREATED
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{create_user2.text}",
        )

        received: str = block_response.status_code
        expected: str = status.HTTP_200_OK
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{block_response.text}",
        )

        received: str = request_response.status_code
        expected: str = status.HTTP_400_BAD_REQUEST
        self.assertEqual(
            received,
            expected,
            msg=f"Expected {expected} status code, received {received}.\n"
            + f"{request_response.text}",
        )