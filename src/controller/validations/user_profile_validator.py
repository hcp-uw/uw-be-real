from marshmallow import (
    Schema,
    fields,
)

from src.model.constants.validation_messages import *


class UserProfileValidator(Schema):
    netid = fields.Str(
        required=True,
        error_messages={"required": NETID_ERROR},
    )
