from marshmallow import (
    Schema,
    fields,
)

from src.model.constants.validation_messages import *

class ReactionCreateValidator(Schema):
    reaction_uri = fields.Str(
        required=True
    )
    net_id = fields.Str(
        required=True
    )
    post_id = fields.Str(
        required=True
    )
