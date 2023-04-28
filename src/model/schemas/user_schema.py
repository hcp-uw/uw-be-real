# Constants imports
from src.model.constants.schema_constants import *

# Schema imports
from src.model.schemas.post_schema import *

SIMPLE_USER_SCHEMA = {
    "netid": {"required": True, "type": NETID},
    "username": {"required": True, "type": "string"},
    "fullname": {"required": True, "type": FULLNAME_REGEX},
}

USER_API_SCHEMA = {
    "info": {
        "type": "dict",
        "schema": {
            # Required properties
            "username": {"required": True, "type": "string"},
            "fullname": {"required": True, "type": "string", "regex": FULLNAME_REGEX},
            "netid": {"required": True, "type": NETID},
            "email": {
                "required": True,
                "type": "string",
                "regex": UW_EMAIL_REGEX,
            },
            "friends": {"required": True, "type": "list", "schema": {"type": NETID}},
            # Optional properties
            "phone": {"required": False, "type": "string", "regex": PHONE_REGEX},
            "birthdate": {"required": False, "type": "datetime", "coerce": TO_DATE},
            "campus": {"required": False, "type": "string", "regex": UW_CAMPUS_REGEX},
            "major": {"required": False, "type": "string"},
            "interests": {
                "required": False,
                "type": "list",
                "schema": {"type": "string"},
            },
        },
    },
    "activity": {
        "type": "dict",
        "schema": {
            "daily_post": {
                "required": False,
                "type": "dict",
                "schema": POST_API_SCHEMA,
            },
        },
    },
}
