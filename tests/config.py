import sys  # for import from parent directory
import os  # for import from parent directory

# add root directory to path
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

# Configs
from src.config import ENV

# Model imports
from src.model.data_access.user_network import UserNetwork
from src.model.queries.neo4j_queries import (
    delete_all_friends,
    delete_all_users,
)

# Note: Python modules are singletons by definition.
BASE_URL: str = "http://127.0.0.1:5555"
USER_NETWORK: UserNetwork = UserNetwork(ENV.neo4j_creds)


def clear_database() -> None:
    """Deletes all users from the network."""
    USER_NETWORK._database_query(delete_all_friends())
    USER_NETWORK._database_query(delete_all_users())
