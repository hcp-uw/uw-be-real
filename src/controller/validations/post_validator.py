from src.model.constants.validator_constants import *


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
            "author_id": {"required": True, "type": "string"},
            "date": {"required": True, "type": "datetime", "coerce": TO_DATE},
            # Optional properties
            "location": {"required": False, "type": "string"},
        },
    },
    "content": {
        "type": "dict",
        "schema": {
            # Required properties
            "front_image": {"required": True, "type": "string"},
            "back_image": {"required": True, "type": "string"},
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
