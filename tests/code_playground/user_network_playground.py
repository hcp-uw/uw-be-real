import sys  # for import from parent directory
import os  # for import from parent directory

# add src directory to path
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
# system imports
from dotenv import load_dotenv
from time import time
import logging

# unit testing
import unittest

# import UserNetwork
from src.controller.api.user_network import UserNetwork

# import custom exceptions
from src.controller.exceptions.generic_exceptions import *
from src.controller.exceptions.neo4j_exceptions import *

# test user data
USERS = {
    1: ("haosen", "li, haosen", "1", "haosen@uw.edu", "1"),
    2: ("andrew", "kim, andrew", "2", "andrew@uw.edu", "2"),
    3: ("peter", "tran, peter", "3", "peter@uw.edu", "3"),
    4: ("alan", "ly, alan", "4", "alan@uw.edu", "4"),
    5: ("anthony", "le, anthony", "5", "anthony@uw.edu", "5"),
    6: ("hai dang", "n, hai dang", "6", "haidang@uw.edu", "6"),
    7: ("steven", "tran, steven", "7", "steven@uw.edu", "7"),
}

FRIENDS = {
    1: [2, 3, 4],
    2: [1, 5, 6],
    3: [5, 7],
}


def main():
    logger = logging.getLogger()

    # load secrets
    neo4j_env_path = os.path.join(os.getcwd(), "secrets", "neo4j", ".env")
    load_dotenv(neo4j_env_path)

    # load credentials and connect to Neo4j database
    n4j_uri = os.getenv("NEO4J_URI")
    n4j_user = os.getenv("NEO4J_USERNAME")
    n4j_pw = os.getenv("NEO4J_PASSWORD")

    un = UserNetwork((n4j_uri, n4j_user, n4j_pw), logger)

    un.create_user("haosenli", "Li, Haosen", "123456789", "haosen@uw.edu", "2041239958")


if __name__ == "__main__":
    main()
