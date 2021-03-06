import enum

class PayloadValidationErrorCodes(enum.Enum):
    pattern = {
        "error_code": "INVALID_FORMAT",
        "error_message": "invalid '{field}' format. Ensure that value entered is valid"
    }
    minLength = {
        "error_code": "INVALID_LENGTH",
        "error_message": "Invalid '{field}' length. Minimum allowed is {value}"
    }
    maxLength = {
        "error_code": "INVALID_LENGTH",
        "error_message": "Invalid '{field}' length. Maximum allowed is {value}"
    }
    required = {
        "error_code": "REQUIRED_FIELD",
        "error_message": "'{field}' is a mandatory field"
    }
    enum = {
        "error_code": "INVALID_CHOICE",
        "error_message": "'{field}' should be one of {value}"
    }
    minimum = {
        "error_code": "MINIMUM_VALUE",
        "error_message": "'{field}' must be greater than equal to {value}"
    }
    maximum = {
        "error_code": "MAXIMUM_VALUE",
        "error_message": "'{field}' must be less than equal to {value}"
    }
    exclusiveMin = {
        "error_code": "EX_MIN_VALUE",
        "error_message": "'{field}' must be greater than {value}"
    }
    exclusiveMax = {
        "error_code": "EX_MAX_VALUE",
        "error_message": "'{field}' must be less than {value}"
    }
    anyOf = {
        "error_code": "INVALID_VALUE",
        "error_message": "Incorrect value entered for '{field}'"
    }
    type = {
        "error_code": "INVALID_VALUE_TYPE",
        "error_message": "'{field}' should be of type {value}"
    }


class FibonacciExecutionError(enum.Enum):
    FIBONACCI_RUNTIME_ERROR ="Error while calculating fibonacci series number"
    NEGATIVE_NUMBER = "Given input is invalid. Please enter number greater than 0"


class FactorialExecutionError(enum.Enum):
    FACTORIAL_RUNTIME_ERROR ="Error while calculating factorial of given number"
    NEGATIVE_NUMBER = "Given input is invalid. Please enter number greater than 0"


class AckermannExecutionError(enum.Enum):
    ACKERMANN_RUNTIME_ERROR ="Error while calculating ackermann value of given numbers"
    NEGATIVE_NUMBER = "Given inputs is invalid. Please enter numbers greater than 0"