# Flask imports
from werkzeug.datastructures import FileStorage

# Marshallow imports
from marshmallow import (
    Schema,
    fields,
    ValidationError,
)

# Regex
import re

# Controller imports
from src.controller.exceptions.post_exceptions import InvalidImagesException

# Model imports
from src.model.constants.validation_messages import NETID_ERROR
from src.model.constants.generic_constants import (
    CAPTION_MAX_CHAR,
    IMAGE_EXTENSION_REGEX,
    ALLOWED_IMAGE_EXTENSIONS,
)


def validate_caption(caption: str) -> None:
    if len(caption) > CAPTION_MAX_CHAR:
        raise ValidationError(f"Caption cannot exceed {CAPTION_MAX_CHAR} characters.")


def validate_images(images: list[FileStorage]) -> None:
    if len(images) != 2:
        raise InvalidImagesException(f"Expected 2 images, received {len(images)}")

    for image in images:
        if re.match(IMAGE_EXTENSION_REGEX, image.filename):
            continue
        raise InvalidImagesException(
            f"Unexpected image extension from {image.filename}. Only {', '.join(ALLOWED_IMAGE_EXTENSIONS)} are allowed."
        )


class MetaData(Schema):
    author_id = fields.Str(
        required=True,
        error_messages={"required": NETID_ERROR},
    )
    location = fields.Str(required=False)
    is_global = fields.Bool(required=True)


class Content(Schema):
    # Images are validated in API Resource
    caption = fields.Str(
        required=False,
        validate=validate_caption 
    )


class PostCreateValidator(Schema):
    metadata = fields.Nested(MetaData)
    content = fields.Nested(Content)
