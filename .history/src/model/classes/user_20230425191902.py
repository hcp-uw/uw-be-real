class User:
    """The User class is a data encapsulator for user information."""
    def __init__(self, user_details: dict) -> None:
        self.username: str
        self.fullname: str
        self.netid: str
        
    def _parse_user_details(self, user_details: dict) -> None:
        """Parse the user details and set the user attributes.
        
        Args: 
            user_details (dict): A dict of user details containing the 
                following (key: value) information on a user:
                - username (str): a str username.
                - fullname (str): a comma separated full name (last, first) or (last,first m.).
                - netid (str): a unique UW NetID.
        """
        self.username = user_details.get("username", "")
        self.fullname = user_details.get("fullname", "")
        self.netid = user_details.get("netid", "")