class AlreadyPostedTodayException(Exception):
    """Raised when the user has already made a post today."""

    def __init__(self) -> None:
        self.msg = f"The user has already made a post today."

    def __str__(self) -> str:
        return self.msg


class InvalidImagesException(Exception):
    """Invalid image related exceptions."""

    def __init__(self, msg) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return self.msg
