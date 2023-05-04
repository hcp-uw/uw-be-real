# Enums
ALLOWED_IMAGE_EXTENSIONS = ["jpg", "jpeg", "png"]

# Regex Constants
PROFILE_IMAGE_EXTENSION_REGEX = f"^\S+/\S+.({'|'.join(ALLOWED_IMAGE_EXTENSIONS)})$"

POST_IMAGE_EXTENSION_REGEX = (
    f"^(post_images/|post_reactions/)\S+.({'|'.join(ALLOWED_IMAGE_EXTENSIONS)})$"
)
