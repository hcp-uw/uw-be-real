class FriendsAlreadyException(Exception):
    """Raised when the user does not exist."""

    def __init__(self, netid1: str, netid2: str) -> None:
        self.msg = f'"{netid1}" is aleady friends with {netid2}.'

    def __str__(self) -> str:
        return self.msg