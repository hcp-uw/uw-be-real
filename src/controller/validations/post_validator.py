from datetime import datetime

# For (Coerce) Cerberus Validator to accept datetime in YYYY-MM-DD format.
to_date = lambda s: datetime.strptime(s, "%Y-%m-%d")

POST_SCHEMA = {
    "post_id": {
        "required": True,
        "type": "string",
        "regex": "^[0-9(a-f|A-F)]{8}-[0-9(a-f|A-F)]{4}-4[0-9(a-f|A-F)]{3}-[89ab][0-9(a-f|A-F)]{3}-[0-9(a-f|A-F)]{12}$",
    },
    "author_id": {"required": True, "type": "string"},
    "date": {"required": True, "type": "datetime", "coerce": to_date},
}
