from marshmallow import (
    Schema,
    fields,
)

from src.model.constants.validation_messages import *

class CommentCreateValidator(Schema):
    comment = fields.Str(
        required=True
    )
    commenter_id = fields.Str(
        required=True
    )
    post_id = fields.Str(
        required=True
    )
