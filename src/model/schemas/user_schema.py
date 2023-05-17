# Constants imports
from src.model.constants.schema_constants import *

# Schema imports
from src.model.schemas.post_schema import *

SIMPLE_USER_SCHEMA = {
    "netid": {
        "required": True,
        "type": NETID,
    },
    "username": {
        "required": True,
        "type": "string",
        "regex": USERNAME_REGEX,
    },
    "fullname": {
        "required": True,
        "type": "string",
        "regex": FULLNAME_REGEX,
    },
    "profile-image": {
        "required": True,
        "type": URL,
    },
    "account-status": {
        "required": True,
        "type": "string",
        "regex": ACCOUNT_STATUS_REGEX,
    },
}

USER_API_SCHEMA = {
    "info": {
        "type": "dict",
        "schema": {
            # Required properties
            "netid": {
                "required": True,
                "type": NETID,
            },
            "username": {
                "required": True,
                "type": "string",
                "regex": USERNAME_REGEX,
            },
            "fullname": {
                "required": True,
                "type": "string",
                "regex": FULLNAME_REGEX,
            },
            "profile-image": {
                "required": True,
                "type": URL,
            },
            "account-status": {
                "required": True,
                "type": "string",
                "regex": ACCOUNT_STATUS_REGEX,
            },
            "email": {
                "required": True,
                "type": "string",
                "regex": UW_EMAIL_REGEX,
            },
            "friends": {
                "required": True,
                "type": "list",
                "schema": {
                    "type": "dict",
                    "schema": SIMPLE_USER_SCHEMA,
                },
            },
            # Optional properties
            "phone": {
                "type": "string",
                "regex": PHONE_REGEX,
            },
            "birthdate": {
                "type": "datetime",
                "coerce": TO_DATE,
            },
            "campus": {
                "type": "string",
                "regex": UW_CAMPUS_REGEX,
            },
            "major": {
                "type": "string",
            },
            "interests": {
                "type": "list",
                "schema": {"type": "string"},
            },
        },
    },
    "activity": {
        "type": "dict",
        "schema": {
            "daily_post": {
                "type": "dict",
                "schema": POST_API_SCHEMA,
            },
        },
    },
}

# Schema for each API endpoints
# /api/user-create
USER_CREATE_SCHEMA = {
    "email": {
        "required": True,
        "type": "string",
        "regex": UW_EMAIL_REGEX,
    },
    "username": {
        "required": True,
        "type": "string",
        "regex": USERNAME_REGEX,
    },
    "firstname": {
        "required": True,
        "type": "string",
        "regex": FIRSTNAME_REGEX,
    },
    "lastname": {
        "required": True,
        "type": "string",
        "regex": LASTNAME_REGEX,
    },
}

# /api/user-profile
USER_PROFILE_SCHEMA = {
    "username": {
        "required": True,
        "type": "string",
        "regex": USERNAME_REGEX,
    },
    "netid": {
        "required": True,
        "type": NETID,
    },
}
