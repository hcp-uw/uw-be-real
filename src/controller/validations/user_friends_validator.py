from marshmallow import (
    Schema,
    fields,
    ValidationError,
)

# Regex for validation
from re import match

from src.model.constants.validation_messages import *
from model.constants.schema_constants import *

def validate_connection(connection: str) -> None:
    if not (connection == "accept" or connection == "request" or connection == "reject" or connection == "unfriend"):
        raise ValidationError(CONNECTION_ERROR)
    

class UserProfileGetValidator(Schema):
    netid = fields.Str(
        required=True,
        error_messages={"required": NETID_ERROR}
    )

class UserFriendsPutValidator(Schema):
    sender_netid = fields.Str(
        required=True,
        error_messages={"required": NETID_ERROR}
    )
    recipient_netid = fields.Str(
        required=True,
        error_messages={"required": NETID_ERROR}
    )
    connection = fields.Str(
        required=True,
        error_messages={"required": CONNECTION_ERROR},
        validate=validate_connection,
    )