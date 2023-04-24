# Exceptions
from src.controller.exceptions.database_exceptions import *


def validate_credentials(neo4j_creds: tuple[str, str, str]) -> None:
    """Validates the credentials used in instantiating the UserNetwork class.
    Exception is thrown on invalid credentials.

    Args:
        None.

    Returns:
        None.

    Exceptions:
        Throws a ConnectionValuesInvalidException if database/storage credentials are invalid.
    """
    # Neo4j credentials
    if not (neo4j_creds and len(neo4j_creds) == 3):
        # No values passed in
        if not neo4j_creds:
            raise ConnectionValuesInvalidException(
                "Expected a tuple in the form of (uri, user, password) in neo4j_creds, received no values."
            )
        # Incorrect length of values
        raise ConnectionValuesInvalidException(
            f"Expected a tuple in the form of (uri, user, password) in neo4j_creds, received {len(neo4j_creds)} value(s) in tuple instead."
        )
