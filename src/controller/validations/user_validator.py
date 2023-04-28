from datetime import datetime

# For (Coerce) Cerberus Validator to accept datetime in YYYY-MM-DD format.
to_date = lambda s: datetime.strptime(s, "%Y-%m-%d")

USER_SCHEMA = {
    "username": {"required": True, "type": "string"},
    "fullname": {"required": True, "type": "string"},
    "netid": {"required": True, "type": "string"},
    "email": {
        "required": True,
        "type": "string",
        "regex": r"^\S*@uw.edu$",
    },
    "phone": {"type": "string", "regex": r"^(|\d{10})$"},
    "birthdate": {"type": "datetime", "coerce": to_date},
    "major": {"type": "string"},
    "interests": {"type": "list"},
}
