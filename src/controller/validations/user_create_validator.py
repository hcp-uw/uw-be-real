# Marshallow imports
from marshmallow import (
    Schema,
    fields,
    ValidationError,
)

# Regex for validation
from re import match

# Constants imports
from model.constants.validation_messages import *
from model.constants.schema_constants import *


def validate_email(email: str) -> None:
    if not match(UW_EMAIL_REGEX, email):
        raise ValidationError(EMAIL_ERROR)


def validate_username(username: str) -> None:
    if not match(USERNAME_REGEX, username):
        raise ValidationError(USERNAME_ERROR)


def validate_lastname(lastname: str) -> None:
    if not match(LASTNAME_REGEX, lastname):
        raise ValidationError(LASTNAME_ERROR)


def validate_firstname(firstname: str) -> None:
    if not match(FIRSTNAME_REGEX, firstname):
        raise ValidationError(FIRSTNAME_ERROR)


class UserCreateValidator(Schema):
    email = fields.Str(
        required=True,
        error_messages={"required": EMAIL_ERROR},
        validate=validate_email,
    )
    username = fields.Str(
        required=True,
        error_messages={"required": USERNAME_ERROR},
        validate=validate_username,
    )
    lastname = fields.Str(
        required=True,
        error_messages={"required": LASTNAME_ERROR},
        validate=validate_lastname,
    )
    firstname = fields.Str(
        required=True,
        error_messages={"required": FIRSTNAME_ERROR},
        validate=validate_firstname,
    )
