class NoInputsException(Exception):
    """Function expects at least one argument, but none are given."""
    def __init__(self) -> None:
        self.msg = "At least one argument is expected but none are given."
    
    def __str__(self) -> str:
        return self.msg