# Functional constants
CAPTION_MAX_CHAR = 250
ALLOWED_IMAGE_EXTENSIONS = ["jpg", "jpeg", "png"]
DATETIME_FORMAT = "%y/%m/%d %H:%M:%S"
DATE_FORMAT = "%y/%m/%d"

# Regex Constants
PROFILE_IMAGE_EXTENSION_REGEX = f"^\S+/\S+.({'|'.join(ALLOWED_IMAGE_EXTENSIONS)})$"

POST_IMAGE_EXTENSION_REGEX = (
    f"^(post_images/|post_reactions/)\S+.({'|'.join(ALLOWED_IMAGE_EXTENSIONS)})$"
)

IMAGE_EXTENSION_REGEX = f"^\S+.({'|'.join(ALLOWED_IMAGE_EXTENSIONS)})$"
