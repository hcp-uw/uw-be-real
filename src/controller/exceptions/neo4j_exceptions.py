class ConnectionFailureException(Exception):
    """Raised when connection to Neo4j failed."""
    def __init__(self) -> None:
        self.msg = "Unable to connect to Neo4j."
    
    def __str__(self) -> str:
        return self.msg
    
class ConnectionAlreadyClosedException(Exception):
    """Raised when trying to close a closed connection."""
    def __init__(self) -> None:
        self.msg = "Connection to Neo4j is already closed."
        
    def __str__(self) -> str:
        return self.msg
    
class QueryFailureException(Exception):
    """Raised when a query to Neo4j failed."""
    def __init__(self, query: str) -> None:
        self.msg = f"Unable to query {query} to Neo4j."
    
    def __str__(self) -> str:
        return self.msg
