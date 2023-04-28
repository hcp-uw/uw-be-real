# Constants imports
from src.model.constants.schema_constants import *

POST_API_SCHEMA = {
    "metadata": {
        "type": "dict",
        "schema": {
            # Required properties
            "post_id": {
                "required": True,
                "type": "string",
                "regex": UUIDV4_REGEX,
            },
            "author_id": {"required": True, "type": NETID},
            "post_datetime": {"required": True, "type": "datetime"},
            # Optional properties
            "location": {"type": "string"},
        },
    },
    "content": {
        "type": "dict",
        "schema": {
            # Required properties
            "front_image": {"required": True, "type": URL},
            "back_image": {"required": True, "type": URL},
            "caption": {"required": True, "type": "string"},
            "reactions_id": {
                "required": True,
                "type": "string",
                "regex": UUIDV4_REGEX,
            },
            "comments_id": {
                "required": True,
                "type": "string",
                "regex": UUIDV4_REGEX,
            },
        },
    },
}
