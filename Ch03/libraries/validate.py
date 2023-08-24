""" Request validation module """

class InvalidFieldError(ValueError):
    """ InvalidFieldError """
    def __init__(self, field, reason) -> None:
        super().__init__(f"{field}: {reason}")
        self.field = field
        self.reason = reason
