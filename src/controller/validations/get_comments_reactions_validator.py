from marshmallow import (
    Schema,
    fields,
)

from src.model.constants.validation_messages import *

class GetCommentsReactionsValidator(Schema):
    post_id = fields.Str(
        required=True
    )
