class FriendsAlreadyException(Exception):
    """Raised when users are already friends"""

    def __init__(self, netid1: str, netid2: str) -> None:
        self.msg = f'"{netid1}" is already friends with "{netid2}".'

    def __str__(self) -> str:
        return self.msg
class NotFriendsException(Exception):
    """Raised when users are not friends"""

    def __init__(self, netid1: str, netid2: str) -> None:
        self.msg = f'"{netid1}" is not friends with "{netid2}".'

    def __str__(self) -> str:
        return self.msg
class NoFriendRequestException(Exception):
    """Raised when there is no friend request from sender to recipient"""

    def __init__(self, sender_netid: str, recipient_netid: str) -> None:
        self.msg = f'No present friend request from "{sender_netid}" to "{recipient_netid}".'

    def __str__(self) -> str:
        return self.msg


