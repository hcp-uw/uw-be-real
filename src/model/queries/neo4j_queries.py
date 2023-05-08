def unique_property_constraint(constraint: str, property: str) -> str:
    return f"""
        CREATE CONSTRAINT {constraint}
        IF NOT EXISTS
        FOR (user:User)
        REQUIRE user.{property} IS UNIQUE;
    """


def create_user(username: str, fullname: str, netid: str, email: str) -> str:
    return f"""
        CREATE (user:User{{
        username: '{username}', 
        fullname: '{fullname}', 
        netid: '{netid}', 
        email: '{email}'
        }})
    """


def get_user(props: list[str]) -> str:
    return f"""
        MATCH (user:User{{{', '.join(props)}}})
        RETURN user
    """


def get_friends(netid: str) -> str:
    return f"""
        MATCH (user: User{{netid: '{netid}'}})-[:Friend]-(friend) 
        RETURN 
            friend.netid AS netid,
            friend.username AS username,
            friend.fullname AS fullname,
            friend.profile_image AS profile_image,
            friend.account_status AS account_status
    """


def check_unique(props: list[str]) -> str:
    return f"""
        MATCH (user:User{{{', '.join(props)}}})
        RETURN user.username AS username
    """


def delete_user(netid: str) -> str:
    return f"""
        MATCH (user:User{{netid: '{netid}'}}) DELETE (user)
    """


def connect_users(sender_netid: str, recipient_netid: str) -> str:
    return f"""
        MATCH (sender: User {{netid: '{sender_netid}'}})
        OPTIONAL MATCH (recipient: User {{netid: '{recipient_netid}'}})
        WHERE recipient IS NOT NULL
        CREATE (sender)-[connect: Friend]->(recipient)
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
