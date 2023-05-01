# Enums
ALLOWED_IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "gif"]

# Regex Constants
IMAGE_EXTENSION_REGEX = (
    f"^(post_images/|post_reactions/)\S+.({'|'.join(ALLOWED_IMAGE_EXTENSIONS)})$"
)
