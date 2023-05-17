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

# TODO: Remove Validation in this


class UserNetwork:
    """The UserNetwork class is a model layer for querying Neo4j
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
            ConnectionValuesInvalidException: Uri, user, or password is invalid.
            ConnectionFailureException: Connection to the database fails.
        """
        # Validate inputs
        validate_user_network_credentials(neo4j_creds)

        # Connect to Neo4j
        self.driver: Driver = self._connect_neo4j(neo4j_creds)

    def _connect_neo4j(self, neo4j_creds: tuple[str, str, str]) -> Driver:
        """Returns a Neo4j Driver from the provided credentials."""
        uri, user, password = neo4j_creds
        return GraphDatabase.driver(uri, auth=(user, password))

    def _close_driver(self) -> None:
        """Close the connection to the database."""
        self.driver.close()

    def _verify_driver(self) -> None:
        """Verifies the driver connection to Neo4j."""
        self.driver.verify_connectivity()

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
            Neo4j Result.

        Exception:
            QueryFailureException: The query caused an error.
        """
        with self.driver.session() as session:
            try:
                result: Result = session.run(query)
            except Exception:
                raise neo4j_exceptions.QueryFailureException(query)
        return result

    def create_user(
        self,
        username: str,
        firstname: str,
        lastname: str,
        netid: str,
        email: str,
    ) -> None:
        """Create a new user in the database.

        Args:
            username (str): The display name of the new user.
            firstname (str): The first name of the new user.
            lastname (str): The last name of the new user.
            netid (str): A [unique] UW NetID of the new user.
            email (str): A [unique] email of the new user.

        Returns:
            None.

        Exceptions:
            NoInputsException: The given netid is invalid.
            UserAlreadyExistsException: User already exists, no changes are made.
            QueryFailureException: An error occured with the query.
        """
        # check if user already exists
        user = self.get_user(netid)
        if user:
            raise neo4j_exceptions.UserAlreadyExistsException(netid)

        query = neo4j_queries.create_user(
            username, firstname, lastname, netid, email, "active"
        )
        self._database_query(query)

    def get_user(self, netid: str) -> dict:
        """Returns all user information associated with the given
        netid. Returns None if no user matches.

        Args:
            netid (str): The netid of the user.

        Returns:
            A dict of information of the associated user.
            If no users can be matched, an empty dict is returned.

        Exceptions:
            NoInputsException: Either the given netid or email is invalid.
            UserNotFoundException: User is not found.
        """
        # Verify arguments
        if not netid:
            raise generic_exceptions.NoInputsException()

        # Start session
        with self.driver.session() as session:
            result = session.execute_read(self._get_user, netid)

        return result

    @staticmethod
    def _get_user(tx, netid: str):
        """Transaction function to get a user's information."""
        query: str = neo4j_queries.get_user(netid)
        result: Record = tx.run(query)
        data: list[dict] = result.data()
        return data[0]["user"] if data else {}

    def get_friends(self, netid: str) -> list[str]:
        """Returns a list of friend information from a user netid."""
        # start session
        with self.driver.session() as session:
            result = session.execute_read(self._get_friends, netid)
        return result

    @staticmethod
    def _get_friends(tx, netid: str) -> list[dict]:
        """Transaction function to return a list of friend information."""
        query = neo4j_queries.get_friends(netid)
        result: Record = tx.run(query)
        return result

    def check_unique(self, netid: str = None, email: str = None) -> bool:
        """Checks if a user already exists by their netid or email."""
        # verify arguments
        if not (netid or email):
            raise generic_exceptions.NoInputsException()

        # start session
        with self.driver.session() as session:
            result = session.execute_read(self._check_unique, netid, email)
        return not bool(result)

    @staticmethod
    def _check_unique(tx, netid: str, email: str) -> str:
        """Transaction function to check if a user already exists."""
        props = []
        if netid:
            props.append(f'netid: "{netid}"')
        if email:
            props.append(f'email: "{email}"')
        query: str = neo4j_queries.check_unique(props)
        result: Record = tx.run(query)
        return result.value("username", "")

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
