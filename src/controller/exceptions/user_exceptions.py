class UserNotFoundException(Exception):
    """Raised when the user does not exist."""

    def __init__(self, netid: str) -> None:
        self.msg = f'"{netid}" is not an existing user.'

    def __str__(self) -> str:
        return self.msg