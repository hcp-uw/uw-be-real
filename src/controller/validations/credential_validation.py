# Exceptions
from src.controller.exceptions.database_exceptions import *


def validate_user_network_credentials(neo4j_creds: tuple[str, str, str]) -> None:
    """Validates the credentials used in instantiating the UserNetwork class.
    Exception is thrown on invalid credentials.

    Args:
        neo4j_creds (tuple): Should contain the following Neo4j credentials in order:
            - uri (str): The URI of the database to connect to.
            - user (str): The username for the database.
            - password (str): The password for the database.

    Returns:
        None.

    Exceptions:
        Throws a ConnectionValuesInvalidException if database/storage credentials are invalid.
    """
    if not neo4j_creds:
        # No values passed in
        raise ConnectionValuesInvalidException(f"No credentials given for Neo4j.")

    if len(neo4j_creds) != 3:
        # Incorrect length of values
        raise ConnectionValuesInvalidException(
            f"Expected a tuple in the form of (uri, user, password) in neo4j_creds, received {len(neo4j_creds)} value(s) in tuple instead."
        )

    if not (neo4j_creds[0] and neo4j_creds[1] and neo4j_creds[2]):
        # Invalid values
        raise ConnectionValuesInvalidException(
            "Some or all of the Neo4j credentials provided are None."
        )


def validate_user_content_credentials(
    s3_creds: tuple[str, str],
    mongo_uri: str,
    redis_creds: tuple[str, str, str],
) -> None:
    """Validates the credentials used in instantiating the UserContent class.
    Exception is thrown on invalid credentials.

    Args:
        s3_creds (tuple): Should contain the following AWS S3 credentials in order:
            - aws_access_key_id (str): A valid AWS IAM user's access key id.
            - aws_secret_access_key (str): A valid AWS IAM user's secret access key.

        mongo_uri (str): The URI of the database to connect to.
            Username and password should be included in the URI.

        redis_creds (tuple): Should contain the following Redis credentials in order:
            - host (str): The hostname of the Redis database to connect to.
            - port (int): The port number of the Redis database.
            - password (str): The password for the Redis database.

    Returns:
        None.

    Exceptions:
        Throws a ConnectionValuesInvalidException if database/storage credentials are invalid.
    """
    # AWS S3 credentials
    if not s3_creds:
        # No values passed in
        raise ConnectionValuesInvalidException(f"No credentials given for AWS S3.")

    if len(s3_creds) != 2:
        # Incorrect length of values
        raise ConnectionValuesInvalidException(
            f"Expected a tuple in the form of (aws_access_key_id, aws_secret_access_key) in s3_creds, received {len(s3_creds)} value(s) in tuple instead."
        )

    if not (s3_creds[0] and s3_creds[1]):
        # Invalid values
        raise ConnectionValuesInvalidException(
            "Some or all of the AWS S3 credentials provided are invalid (None)."
        )

    # MongoDB credentials
    if not mongo_uri:
        raise ConnectionValuesInvalidException(
            "Expected a uri connection string for MongoDB, received no value."
        )

    # Redis credentails
    if not redis_creds:
        # No values passed in
        raise ConnectionValuesInvalidException(f"No credentials given for Redis.")

    if len(redis_creds) != 3:
        # Incorrect length of values
        raise ConnectionValuesInvalidException(
            f"Expected a tuple in the form of (host, port, password) in redis_creds, received {len(redis_creds)} value(s) in tuple instead."
        )

    if not (redis_creds[0] and redis_creds[1] and redis_creds[2]):
        # Invalid values
        raise ConnectionValuesInvalidException(
            "Some or all of the Redis credentials provided are None."
        )
