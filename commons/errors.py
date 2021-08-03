class Error(Exception):
    """
    This signifies the error being raise from various validators
    """

    def __init__(self, error_code, error_message):
        self.error_code = error_code
        self.error_message = error_message

    def __eq__(self, error):
        """Checks if error objects are equal"""

        try:
            assert (self.error_code == error.error_code)
            assert (self.error_message == error.error_message)
        except AssertionError:
            return False
        return True

    def to_dict(self):
        return {
            "error_code": self.error_code,
            "error_message": self.error_message
        }