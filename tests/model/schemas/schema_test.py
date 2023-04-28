import sys  # for import from parent directory
from os.path import (
    dirname,  # for import from parent directory
    realpath,  # gets current path
)

# Add src directory to path
current = dirname(realpath(__file__))
top = dirname(dirname(dirname(current)))

sys.path.append(top)

from datetime import datetime
from cerberus import Validator

from src.model.schemas.user_schema import *
from src.model.schemas.user_schema_example import *


if __name__ == "__main__":
    v: Validator = Validator()
    v.validate(SIMPLE_USER_SCHEMA_EX, SIMPLE_USER_SCHEMA)
    print(v.errors)

    v.validate(USER_API_SCHEMA_EX, USER_API_SCHEMA)
    print(v.errors)
