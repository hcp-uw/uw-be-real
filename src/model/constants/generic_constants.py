# Enums
ALLOWED_IMAGE_EXTENSIONS = ["jpg", "jpeg", "png", "gif"]

# Regex Constants
IMAGE_EXTENSION_REGEX = f"\S+.({'|'.join(ALLOWED_IMAGE_EXTENSIONS)})$"
