from model.constants.schema_constants import *


REACTIONS_API_SCHEMA = {
    "type": "list",
    "schema": {
        "type": "dict",
        "schema": {
            "author_id": {"required": True, "type": NETID},
            "author_username": {"required": True, "type": "string"},
            "author_fullname": {"required": True, "type": FULLNAME_REGEX},
            "reaction_id": {"required": True, "type": UUIDV4_REGEX},
            "reaction_image": {"required": True, "type": URL},
        },
    },
}

COMMENTS_API_SCHEMA = {"type": "list", "schema": {}}
