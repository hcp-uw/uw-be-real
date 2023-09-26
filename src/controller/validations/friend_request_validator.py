from marshmallow import (
    Schema,
    fields,
)

from src.model.constants.validation_messages import *


class FriendRequestSendValidator(Schema):
    sender_netid = fields.Str(
        required=True,
        error_messages={"required": NETID_ERROR},
    )
    recipient_netid = fields.Str(
        required=True, 
        error_messages={"required": NETID_ERROR}
    )

class FriendRequestRespondValidator(Schema): 
    sender_netid = fields.Str(
        required=True,
        error_messages={"required": NETID_ERROR},
    )
    recipient_netid = fields.Str(
        required=True, 
        error_messages={"required": NETID_ERROR}
    )
    accept = fields.Bool(
        required=True, 
        error_message={"required": ACCEPT_ERROR}
    )