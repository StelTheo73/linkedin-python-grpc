""" Client exceptions """

class ClientError(Exception):
    """ Generic client exception """
    def __init__(self, code, details) -> None:
        super().__init__(f"\n\nerror code: {code}\n\ndetails: {details}")
        self.code = code
        self.details = details
