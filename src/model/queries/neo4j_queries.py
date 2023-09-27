def unique_property_constraint(constraint: str, property: str) -> str:
    return f"""
        CREATE CONSTRAINT {constraint}
        IF NOT EXISTS
        FOR (user:User)
        REQUIRE user.{property} IS UNIQUE;
    """


def create_user(
    username: str,
    firstname: str,
    lastname: str,
    netid: str,
    email: str,
    account_status: str = "active",
) -> str:
    return f"""
        CREATE (user:User{{
        username: '{username}', 
        firstname: '{firstname}', 
        lastname: '{lastname}', 
        netid: '{netid}', 
        email: '{email}',
        account_status: '{account_status}'
        }})
    """


def get_user(netid: str) -> str:
    return f"""
        MATCH (user:User{{netid: "{netid}"}})
        RETURN user
    """


def get_friends(netid: str) -> str:
    return f"""
        MATCH (user: User{{netid: '{netid}'}})-[:Friend]-(friend) 
        WHERE (user)-[:Friend]-(friend) AND (friend)-[:Friend]-(user)
        RETURN 
            friend.netid AS netid,
            friend.username AS username,
            friend.firstname AS firstname,
            friend.lastname AS lastname,
            friend.profile_image AS profile_image,
            friend.account_status AS account_status
    """
def get_incoming_friend_requests(netid: str) -> str: 
    return f"""
        MATCH (user: User{{netid: '{netid}'}})<-[:SentFriendRequestTo]-(friend) 
        RETURN 
            friend.netid AS netid,
            friend.username AS username,
            friend.firstname AS firstname,
            friend.lastname AS lastname,
            friend.profile_image AS profile_image,
            friend.account_status AS account_status
    """
def check_friend_request(sender_netid: str, recipient_netid: str) -> str: 
    return f""" 
        MATCH (user: User{{netid: '{sender_netid}'}})-[:SentFriendRequestTo]->(friend: User{{netid: '{recipient_netid}'}})
        RETURN user.username AS username
    """
def check_unique(props: list[str]) -> str:
    return f"""
        MATCH (user:User{{{', '.join(props)}}})
        RETURN user.username AS username
    """
def check_friend(netid1: str, netid2: str) -> str: 
    return f"""
        MATCH (: User{{netid: '{netid1}'}})-[f:Friend]-(: User{{netid: '{netid2}'}})
        RETURN f AS friend
    """

def delete_user(netid: str) -> str:
    return f"""
        MATCH (user:User{{netid: '{netid}'}}) DELETE (user)
    """

def search_users(netid: str, search_str: str) -> str: 
    return f"""
        MATCH (user: User)
        WHERE user.username STARTS WITH '{search_str}' AND NOT (user)-[:Blocked]-(:User{{netid: '{netid}'}}) AND NOT user.netid = '{netid}' 
        RETURN user.netid AS netid,
            user.username AS username,
            user.firstname AS firstname,
            user.lastname AS lastname,
            user.profile_image AS profile_image,
            user.account_status AS account_status
        LIMIT 50
    """

def connect_users(sender_netid: str, recipient_netid: str) -> str:
    return f"""
        MATCH (sender: User {{netid: '{sender_netid}'}})-[r:SentFriendRequestTo]->(recipient: User {{netid: '{recipient_netid}'}})
        DELETE r
        MERGE (sender)-[:Friend]-(recipient)
    """

    """
        MATCH (sender: User {{netid: '{sender_netid}'}})
        MATCH (recipient: User {{netid: '{recipient_netid}'}})
        WHERE NOT (sender)-[:Friend]-(recipient)
        DELETE (sender)-[:SentFriendRequestTo]-(recipient)
        MERGE (sender)-[:Friend]-(recipient)
        """
    """
        MATCH (sender: User {{netid: '{sender_netid}'}})
        OPTIONAL MATCH (recipient: User {{netid: '{recipient_netid}'}})
        WHERE recipient IS NOT NULL
        CREATE (sender)-[connect: Friend]->(recipient)
    """

def send_friend_request(sender_netid: str, recipient_netid: str) -> str: 
    return f"""
        MATCH (sender: User {{netid: '{sender_netid}'}})
        MATCH (recipient: User {{netid: '{recipient_netid}'}})
        WHERE NOT (sender)-[:Friend]-(recipient)
        MERGE (sender)-[:SentFriendRequestTo]->(recipient)
    """

def remove_friend_request(sender_netid: str, recipient_netid: str) -> str: 
    return f"""
        MATCH (sender: User {{netid: '{sender_netid}'}})-[r:SentFriendRequestTo]->(recipient: User {{netid: '{recipient_netid}'}})
        DELETE r
    """
def remove_friend(sender_netid: str, recipient_netid: str) -> str: 
    return f"""
        MATCH (sender: User {{netid: '{sender_netid}'}})-[r:Friend]-(recipient: User {{netid: '{recipient_netid}'}})
        DELETE r
    """ 

def block_user(sender_netid: str, recipient_netid: str) -> str: 
    return f"""
        MATCH (sender: User {{netid: '{sender_netid}'}})-[r]-(recipient: User {{netid: '{recipient_netid}'}})
        DELETE r 
        MERGE (sender)-[:Blocked]->(recipient)
    """

def unblock_user(sender_netid: str, recipient_netid: str) -> str: 
    return f"""
        MATCH (sender: User {{netid: '{sender_netid}'}})-[block: Blocked]->(recipient: User {{netid: '{recipient_netid}'}})
        DELETE block
    """

def check_block(blocker_netid: str, blocked_netid: str) -> str: 
    return f"""
        MATCH (: User{{netid: '{blocker_netid}'}})-[b:Blocked]->(: User{{netid: '{blocked_netid}'}})
        RETURN b as blocked
    """
# DO NOT USE THESE IN ACTUAL APPLICATION. TESTING ONLY.
def delete_all_users() -> str:
    return """
        MATCH (user: User) DELETE (user)
    """


def delete_all_friends() -> str:
    return """
        MATCH ()-[f:Friend]-() DELETE (f)
    """
def delete_all_friend_requests() -> str: 
    return """
        MATCH ()-[request:SentFriendRequestTo]-() DELETE (request)
    """