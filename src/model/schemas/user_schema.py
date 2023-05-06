# Constants imports
from src.model.constants.schema_constants import *
from src.model.constants.schema_error_messages import *

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

CREATE_USER_SCHEMA = {
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
    "fullname": {
        "required": True,
        "type": "string",
        "regex": FULLNAME_REGEX,
    },
}

CREATE_USER_SCHEMA_ERROR_MSG = {
    "email": EMAIL_ERROR,
    "username": USERNAME_ERROR,
    "fullname": FULLNAME_ERROR,
}
