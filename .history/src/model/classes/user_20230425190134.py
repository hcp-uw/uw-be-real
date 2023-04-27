class User:
    """The User class is a data encapsulator for user information."""
    def __init__(self, username: str, fullname: str, netid: str) -> None:
        self.username: str = username
        self.fullname: str = fullname
        self.netid: str = netid