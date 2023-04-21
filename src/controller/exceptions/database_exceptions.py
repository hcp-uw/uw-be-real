class ConnectionFailureException(Exception):
    """Raised when connection to database failed."""
    def __init__(self, db_name: str) -> None:
        self.msg = f"Unable to connect to {db_name}."
    
    def __str__(self) -> str:
        return self.msg

class ConnectionValuesInvalidException(Exception):
    """Raised when there are at least one invalid connection argument."""
    def __init__(self, db_name: str) -> None:
        self.msg = f"One or more of the connection arguments are invalid for {db_name}."
    
    def __str__(self) -> str:
        return self.msg
    
