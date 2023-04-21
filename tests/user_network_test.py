import sys # for import from parent directory
import os # for import from parent directory
# add src directory to path
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
# system imports
from dotenv import load_dotenv
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
    1: ('haosen', 'li, haosen', '1', 'haosen@uw.edu', '1'),
    2: ('andrew', 'kim, andrew', '2', 'andrew@uw.edu', '2'),
    3: ('peter', 'tran, peter', '3', 'peter@uw.edu', '3'),
    4: ('alan', 'ly, alan', '4', 'alan@uw.edu', '4'),
    5: ('anthony', 'le, anthony', '5', 'anthony@uw.edu', '5'),
    6: ('hai dang', 'n, hai dang', '6', 'haidang@uw.edu', '6'),
    7: ('steven', 'tran, steven', '7', 'steven@uw.edu', '7'),
}

FRIENDS = {
    1: [2, 3, 4],
    2: [1, 5, 6],
    3: [5, 7],   
}

class UserNetworkTest(unittest.TestCase):
    """Performs unit testing on the UserNetwork class."""
    def __init__(self, method_name: str = ...) -> None:
        super().__init__(method_name)
        
        # Create a logger object
        self.logger = logging.getLogger()
        
        # load secrets
        neo4j_env_path = os.path.join(os.getcwd(), 'secrets', 'neo4j', '.env')
        load_dotenv(neo4j_env_path)

        # load credentials and connect to Neo4j database
        self.n4j_uri = os.getenv('NEO4J_URI')
        self.n4j_user = os.getenv('NEO4J_USERNAME')
        self.n4j_pw = os.getenv('NEO4J_PASSWORD')
        
    def _add_all_users(self, network: UserNetwork) -> None:
        """Add all users to the network."""
        for data in USERS.values():
            username, fullname, netid, email, phone = data
            network.create_user(username, fullname, netid, email, phone)
    
    def _delete_all_users(self, network: UserNetwork) -> None:
        """Deletes all users from the network."""
        network._database_query('MATCH ()-[f:Friend]-() DELETE (f)')
        network._database_query('MATCH (user: User) DELETE (user)')
        
    def _add_all_friends(self, network: UserNetwork) -> bool:
        """Connects all friends to the network."""
        for user, friends in FRIENDS.items():
            for friend in friends:
                try:
                    network.connect_users(user, friend)
                except:
                    return False
        return True
        
    def test_get_user_no_input(self) -> None:
        """Verifies the get_user method."""
        network = UserNetwork((self.n4j_uri, self.n4j_user, self.n4j_pw), self.logger)
        self.assertRaises(NoInputsException, network.get_user)
        
    def test_get_user_one_input(self) -> None:
        """Verifies the get_user method with one arg."""
        network = UserNetwork((self.n4j_uri, self.n4j_user, self.n4j_pw), self.logger)
        for netid, data in USERS.items():
            username = network.get_user(str(netid))['username']
            self.assertEqual(username, data[0])
    
    # def test_check_unique(self) -> None:
    #     """TODO: Verifies the check_unique method."""
    #     network = UserNetwork(self.n4j_uri, self.n4j_user, self.n4j_pw)
    #     is_unique = network.check_unique(netid='1')

    def test_create_and_verify_users(self) -> None:
        """Verifies the create_user and get_username_by_netid methods."""
        network = UserNetwork((self.n4j_uri, self.n4j_user, self.n4j_pw), self.logger)
        self._delete_all_users(network)
        self._add_all_users(network)
        # verify and delete all test users
        for netid, data in USERS.items():
            username = network.get_user(str(netid))['username']
            self.assertEqual(username, data[0])
        
    def test_connect_users(self):
        """Tests the connect_users method."""
        network = UserNetwork((self.n4j_uri, self.n4j_user, self.n4j_pw), self.logger)
        self._delete_all_users(network)
        self._add_all_users(network)
        add_success = self._add_all_friends(network)
        self.assertTrue(add_success)     
        
    def test_get_friends(self):
        """Tests the get_friends method."""
        network = UserNetwork((self.n4j_uri, self.n4j_user, self.n4j_pw), self.logger)
        self._delete_all_users(network)
        self._add_all_users(network)
        add_success = self._add_all_friends(network)
        self.assertTrue(add_success)
        for user, friends in FRIENDS.items():
            n_friends = network.get_friends(str(user))
            n_friends = set(n_friends)
            for friend in friends:
                if str(friend) not in n_friends:
                    self.assertFalse(True)          
            
if __name__ == '__main__':
    unittest.main()