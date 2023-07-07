# Constants imports
from src.model.constants.schema_constants import *

REDIS_POST_SCHEMA = {
    "post_id": {
        "required": True,
        "type": "string",
        "regex": UUIDV4_REGEX,
    },
}

REDIS_SCHEMA = {
    "global": {
        "post_id": {
            "type": "string",
            "regex": UUIDV4_REGEX,
        },
        "type": "list",
    },
    "post": {
        "netid": {
            "type": NETID,
            "schema": {
                "type": "dict",
                "schema": REDIS_POST_SCHEMA,
            },
        }
    },
}
