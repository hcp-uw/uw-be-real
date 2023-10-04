from marshmallow import (
    Schema,
    fields,
)

from src.model.constants.validation_messages import *

class GetPostsValidator(Schema):
    is_global = fields.Bool(
        required=True
    )
