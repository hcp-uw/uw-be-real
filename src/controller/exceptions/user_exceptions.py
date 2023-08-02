class UserNotFoundException(Exception):
    """Raised when the user does not exist."""

    def __init__(self, netid: str) -> None:
        self.msg = f'"{netid}" is not an existing user.'

    def __str__(self) -> str:
        return self.msg
    
class ExistingConnectionException(Exception):
    """Raised when the same connection is passed in."""

    def __init__(self) -> None:
        self.msg = "This connection already exists."

    def __str__(self) -> str:
        return self.msg
    
class InvalidConnectionException(Exception):
    """Raised when the wrong connection is passed in."""

    def __init__(self) -> None:
        self.msg = "This connection cannot be used yet."

    def __str__(self) -> str:
        return self.msg