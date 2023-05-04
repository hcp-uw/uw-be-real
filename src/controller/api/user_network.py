# Neo4j imports
from neo4j import GraphDatabase
from neo4j import Result
from neo4j import Record
from neo4j import Driver

# Controller imports
from src.controller.exceptions import *
from src.controller.validations.credential_validation import *

# Model imports
from src.model.constants import *
from src.model.queries import *


class UserNetwork:
    """The UserNetwork class is a Python API layer for querying Neo4j
    specific to social network applications."""

    def __init__(self, neo4j_creds: tuple[str, str, str]) -> None:
        """Creates a new UserNetwork connected to a Neo4j database.

        Args:
            neo4j_creds (tuple): Should contain the following Neo4j credentials:
                - uri (str): The URI of the database to connect to.
                - user (str): The username for the database.
                - password (str): The password for the database.

        Returns:
            None.

        Exceptions:
            Throws a ConnectionValuesInvalidException if uri, user, or password is invalid.
            Throws a ConnectionFailureException if the connection to the database fails.
        """
        # Validate inputs
        validate_user_network_credentials(neo4j_creds)

        # Connect to Neo4j
        self.driver: Driver = self._connect_neo4j(neo4j_creds)

        # TODO: Do we need these? It has high performance impact on cold starts. -> Create an admin account that manages the constraints instead
        # self._verify_driver()
        # self._verify_constraints()

    def __del__(self) -> None:
        """Automatically disconnects the Neo4j driver connection on
        garbage collection or program end."""
        self._close_driver()

    def _connect_neo4j(self, neo4j_creds: tuple[str, str, str]) -> Driver:
        """Returns a Neo4j Driver from the provided credentials."""
        uri, user, password = neo4j_creds
        return GraphDatabase.driver(uri, auth=(user, password))

    def _close_driver(self) -> None:
        """Close the connection to the database.

        Exception:
            Throws a ConnectionAlreadtClosedException if connection is already closed.
        """
        try:
            self.driver.close()
        except Exception as e:
            raise neo4j_exceptions.ConnectionAlreadyClosedException()

    def _verify_driver(self) -> None:
        """Verifies the driver connection to Neo4j.

        Exception:
            Throws a ConnectionFailureException if driver connection is invalid.
        """
        try:
            self.driver.verify_connectivity()
        except Exception:
            raise database_exceptions.ConnectionFailureException(neo4j_constants.NAME)

    def _verify_constraints(self) -> None:
        """Ensures that constraints for unique user properties are added."""
        constraints = neo4j_constants.UNIQUE_USER_PROPERTIES
        for constraint, property in constraints.items():
            # TODO: add validation check for constraint and property
            query = neo4j_queries.unique_property_constraint(constraint, property)
            self._database_query(query)

    def _database_query(self, query: str) -> Result:
        """Executes the given Cypher query.

        Args:
            query (str): The Cypher query to execute.

        Returns:
            Neo4j Result if successful, None otherwise.

        Exception:
            Throws a QueryFailureException if the query caused an error.
        """
        result = None
        with self.driver.session() as session:
            try:
                result = session.run(query)
            except Exception:
                raise neo4j_exceptions.QueryFailureException(query)
        return result

    def create_user(
        self,
        username: str,
        fullname: str,
        netid: str,
        email: str,
        profile_image_url: str,
    ) -> bool:
        """Create a new user in the database and returns True if successful.

        Args:
            username (str): The display name of the new user.
            fullname (str): The full name of the new user (Last, First).
            netid (str): A [unique] UW NetID of the new user.
            email (str): A [unique] email of the new user.
            profile_image_url (str): An image url containing a user's profile picture.

        Returns:
            True if new user is successfully created, False otherwise.
        """
        # check if user already exists
        user = self.get_user(netid)
        if user is not None:
            raise neo4j_exceptions.UserAlreadyExistsException(netid)

        query = neo4j_queries.create_user(
            username, fullname, netid, email, profile_image_url
        )
        self._database_query(query)

    def get_user(self, netid: str = None, email: str = None) -> dict:
        """Returns all user information associated with the given
        netid, email, and/or phone. Returns None if no user matches.

        Args:
            netid (str, optional): The netid of the user.
            email (str, optional): The email of the user.

        Returns:
            A dict of information of the associated user,
            None if no users are associated with the given args.
        """
        # verify arguments
        if not (netid or email):
            raise generic_exceptions.NoInputsException()

        # helper method
        def _get_user(tx):
            props = []
            if netid:
                props.append(f'netid: "{netid}"')
            if email:
                props.append(f'email: "{email}"')
            query = neo4j_queries.get_user(props)
            result: Record = tx.run(query)
            data = result.data()
            if data:
                return data[0]["user"]
            return None

        # start session
        with self.driver.session() as session:
            result = session.execute_read(_get_user)
        return result

    def get_friends(self, netid: str) -> list[str]:
        """Returns a list of friend netids from a user netid."""

        # helper method
        def _get_friends(tx):
            query = neo4j_queries.get_friends(netid)
            result: Record = tx.run(query)
            return result.value("netid")

        # start session
        with self.driver.session() as session:
            result = session.execute_read(_get_friends)
        return result

    def check_unique(self, netid: str = None, email: str = None) -> bool:
        """Checks if a user already exists by their netid or email"""
        # verify arguments
        if not (netid or email):
            raise generic_exceptions.NoInputsException()

        # helper method
        def _check_unique(tx):
            props = []
            if netid:
                props.append(f'netid: "{netid}"')
            if email:
                props.append(f'email: "{email}"')
            query = neo4j_queries.check_unique(props)
            result: Record = tx.run(query)
            return result.value("username", False)

        # start session
        with self.driver.session() as session:
            result = session.execute_read(_check_unique)
        return not bool(result)

    def deactivate_user(self, netid: str) -> None:
        """Deactivates the user associated with the given netid."""
        pass

    def ban_user(self, netid: str, ban_reason: str) -> None:
        """Bans the user associated with the given netid."""
        pass

    def delete_user(self, netid: str) -> None:
        """Deletes a user from the Neo4j database with the given netid."""
        query = neo4j_queries.delete_user(netid)
        self._database_query(query)

    def connect_users(self, sender_netid: str, recipient_netid: str) -> None:
        """Connect two users by their netids."""
        query = neo4j_queries.connect_users(sender_netid, recipient_netid)
        self._database_query(query)
