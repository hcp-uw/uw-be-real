from marshmallow import (
    Schema,
    fields,
)

from src.model.constants.validation_messages import *

class UserSearchValidator(Schema): 
  netid = fields.Str(
    required=True,
    error_messages={"required": NETID_ERROR}
  )
  search_str = fields.Str(
    required = True, 
    error_messages={"required": SEARCH_ERROR}
  )