class User:
    """The User class is a data encapsulator for user information."""
    def __init__(self, user_details: dict) -> None:
        self.username: str
        self.fullname: str
        self.netid: str
        
    def _parse_user_details(self, user_details: dict) -> None:
        """Parse the user details and set the user attributes."""
        self.username = user_details.get("username", "")
        self.fullname = user_details.get("fullname", "")
        self.netid = user_details.get("netid", "")