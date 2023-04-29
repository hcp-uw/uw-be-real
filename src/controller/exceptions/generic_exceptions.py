class NoInputsException(Exception):
    """Function expects at least one argument, but none are given."""

    def __init__(self) -> None:
        self.msg = "At least one argument is expected but none are given."

    def __str__(self) -> str:
        return self.msg


class IncorrectObjectTypeException(Exception):
    """Raised when an incorrect object type is passed in."""

    def __init__(self) -> None:
        self.msg = "An incorrect object is passed in."

    def __str__(self) -> str:
        return self.msg


class IncorrectFileExtensionTypeException(Exception):
    """Raised when an incorrect file extension type is passed in."""

    def __init__(self, error_msg: str) -> None:
        self.msg = error_msg

    def __str__(self) -> str:
        return self.msg
