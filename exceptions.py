from commons.errors import Error

class ExceptionBase(Exception):
    error_code = None
    error_message = None

    def __init__(self, error_code=None, message_params_dict={}, error=None, *args):
        if error and isinstance(error, Error):
            self.error_code = error.error_code
            self.error_message = error.error_message
        else:
            self.error_enum = error_code
            self.error_code = error_code.name
            self.error_message = error_code.value.format(**message_params_dict)
        super(ExceptionBase, self).__init__(self.error_message, *args)

    def to_dict(self):
        return {
            "error_code": self.error_code,
            "error_message": self.error_message
        }


class FibonacciCalculationException(ExceptionBase):
    pass


class FactorialCalculationException(ExceptionBase):
    pass


class AckermannCalculationException(ExceptionBase):
    pass