def unique_property_constraint(constraint: str, property: str) -> str:
    return f"""
        CREATE CONSTRAINT {constraint}
        IF NOT EXISTS
        FOR (user:User)
        REQUIRE user.{property} IS UNIQUE;
    """


def create_user(
    username: str, fullname: str, netid: str, email: str, profile_image_url: str
) -> str:
    return f"""
        CREATE (user:User{{
        username: '{username}', 
        fullname: '{fullname}', 
        netid: '{netid}', 
        email: '{email}', 
        profile-image-url: '{profile_image_url}'
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
        RETURN friend.netid AS netid
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
        MATCH 
            (sender: User), (recipient: User)
        WHERE
            sender.netid = '{sender_netid}' AND recipient.netid = '{recipient_netid}'
        CREATE
            (sender)-[connect: Friend]->(recipient)
    """
