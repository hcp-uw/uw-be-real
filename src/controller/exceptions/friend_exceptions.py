class FriendsAlreadyException(Exception):
    """Raised when users are already friends"""

    def __init__(self, netid1: str, netid2: str) -> None:
        self.msg = f'"{netid1}" is already friends with {netid2}.'

    def __str__(self) -> str:
        return self.msg
class NotFriendsException(Exception):
    """Raised when users are not friends"""

    def __init__(self, netid1: str, netid2: str) -> None:
        self.msg = f'"{netid1}" is not friends with {netid2}.'

    def __str__(self) -> str:
        return self.msg

