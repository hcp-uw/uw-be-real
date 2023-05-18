from marshmallow import (
    Schema,
    fields,
    ValidationError,
)

# Regex for validation
from re import match

from src.model.constants.validation_messages import *
from model.constants.schema_constants import *

def validate_username(username: str) -> None:
    if not match(USERNAME_REGEX, username):
        raise ValidationError(USERNAME_ERROR)
    
def validate_firstname(firstname: str) -> None:
    if not match(FIRSTNAME_REGEX, firstname):
        raise ValidationError(FIRSTNAME_ERROR)

def validate_lastname(lastname: str) -> None:
    if not match(LASTNAME_REGEX, lastname):
        raise ValidationError(LASTNAME_ERROR)
    
def validate_phone(phone: str) -> None:
    if not match(PHONE_REGEX, phone):
        raise ValidationError(PHONE_ERROR)
    
def validate_birthdate(birthdate: str) -> None:
    if not match(DATE_REGEX, birthdate):
        raise ValidationError(DATE_ERROR)
    
def validate_uw_campus(uw_campus: str) -> None:
    if not match(UW_CAMPUS_REGEX, uw_campus):
        raise ValidationError(UW_CAMPUS_ERROR)
    
def validate_major(major: str) -> None:
    if not match(MAJOR_REGEX, major):
        raise ValidationError(MAJOR_ERROR)
    
def validate_interests(interests: list) -> None:
    if not all((match(INTERESTS_REGEX, interest)) for interest in interests):
        raise ValidationError(INTERESTS_ERROR)

class UserProfileGetValidator(Schema):
    netid = fields.Str(
        required=True,
        error_messages={"required": NETID_ERROR}
    )

class UserProfilePutValidator(Schema):
    netid = fields.Str(
        required=True,
        error_messages={"required": NETID_ERROR}
    )
    username = fields.Str(
        required=False,
        error_messages={"required": USERNAME_ERROR},
        validate=validate_username,
    )
    firstname = fields.Str(
        required=False,
        error_messages={"required": FIRSTNAME_ERROR},
        validate=validate_firstname,
    )
    lastname = fields.Str(
        required=False,
        error_messages={"required": LASTNAME_ERROR},
        validate=validate_lastname,
    )
    profileimage = fields.URL(
        required=False,
        error_messages={"required": PROFILEIMAGE_ERROR},
    )
    # friends = fields.List(
    #     required=False,
    #     #error_messages={"required": }
    # )
    phone = fields.Str(
        required=False,
        error_messages={"required": PHONE_ERROR},
        validate=validate_phone,
    )
    birthdate = fields.Date(
        required=False,
        error_messages={"required": DATE_ERROR},
        validate=validate_birthdate,
    )
    campus = fields.Str(
        required=False,
        error_messages={"required": UW_CAMPUS_ERROR},
        validate=validate_uw_campus,
    )
    major = fields.Str(
        required=False,
        error_messages={"required": MAJOR_ERROR},
        validate=validate_major,
    )
    interests = fields.List(
        fields.Str(),
        required=False,
        error_messages={"required": INTERESTS_ERROR},
        validate=validate_interests,
    )