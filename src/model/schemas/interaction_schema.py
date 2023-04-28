# Constants imports
from src.model.constants.schema_constants import *

# Schema imports
from src.model.schemas.user_schema import *

# Single reaction
REACTION_SCHEMA = {
    "type": "dict",
    "schema": {
        "author": {
            "required": True,
            "type": "dict",
            "schema": SIMPLE_USER_SCHEMA,
        },
        "parent_id": {"required": True, "type": "string", "regex": UUIDV4_REGEX},
        "reaction_id": {"required": True, "type": "string", "regex": UUIDV4_REGEX},
        "reaction_image": {"required": True, "type": URL},
        "reaction_datetime": {"required": True, "type": "datetime"},
    },
}

# Reactions section
REACTIONS_API_SCHEMA = {
    "type": "dict",
    "schema": {
        "post_id": {
            "required": True,
            "type": "string",
            "regex": UUIDV4_REGEX,
        },
        "type": "list",
        "schema": REACTION_SCHEMA,
    },
}

# Replies under a comment
COMMENT_REPLIES_SCHEMA = {
    "type": "list",
    "schema": {
        "author": {
            "required": True,
            "type": "dict",
            "schema": SIMPLE_USER_SCHEMA,
        },
        "parent_id": {"required": True, "type": "string", "regex": UUIDV4_REGEX},
        "comment_id": {"required": True, "type": "string", "regex": UUIDV4_REGEX},
        "comment_content": {"required": True, "type": "string"},
        "comment_datetime": {"required": True, "type": "datetime"},
    },
}

# Individual comment
COMMENT_SCHEMA = {
    "type": "dict",
    "schema": {
        "author": {
            "required": True,
            "type": "dict",
            "schema": SIMPLE_USER_SCHEMA,
        },
        "comment_id": {"required": True, "type": "string", "regex": UUIDV4_REGEX},
        "comment_content": {"required": True, "type": "string"},
        "comment_datetime": {"required": True, "type": "datetime"},
        "comment_replies": COMMENT_REPLIES_SCHEMA,
        "tagged_users": {"type": "list", "schema": SIMPLE_USER_SCHEMA},
    },
}

# Comments section
COMMENTS_API_SCHEMA = {
    "type": "dict",
    "schema": {
        "post_id": {
            "required": True,
            "type": "string",
            "regex": UUIDV4_REGEX,
        },
        "type": "list",
        "schema": COMMENT_SCHEMA,
    },
}
