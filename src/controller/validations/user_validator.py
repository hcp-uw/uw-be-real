from src.model.constants.validator_constants import *


USER_API_SCHEMA = {
    "info": {
        "type": "dict",
        "schema": {
            # Required properties
            "username": {"required": True, "type": "string"},
            "fullname": {"required": True, "type": "string"},
            "netid": {"required": True, "type": "string"},
            "email": {
                "required": True,
                "type": "string",
                "regex": UW_EMAIL_REGEX,
            },
            "friends": {"required": True, "type": "list", "schema": {"type": "string"}},
            # Optional properties
            "phone": {"required": False, "type": "string", "regex": PHONE_REGEX},
            "birthdate": {"required": False, "type": "datetime", "coerce": TO_DATE},
            "campus": {"required": False, "type": "string", "regex": UW_CAMPUS_REGEX},
            "major": {"required": False, "type": "string"},
            "interests": {"required": False, "type": "list"},
        },
    },
    "todays_post_id": {"required": False, "type": "string", "regex": UUIDV4_REGEX},
}
