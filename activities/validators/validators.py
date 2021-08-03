from activities.exceptions import NegativeNumberException
from errors import FibonacciExecutionError, FactorialExecutionError, AckermannExecutionError
from logs import logger

from activities.validators.base import ValidatorBase


class FibonacciNumberValidator(ValidatorBase):

    def validate(self):

        number = self.context.number
        logger.info('number is here {}'.format(number))

        if number < 0:
            raise NegativeNumberException(error_code=FibonacciExecutionError.NEGATIVE_NUMBER)


class FactorialNumberValidator(ValidatorBase):

    def validate(self):

        number = self.context.factorial_number
        logger.info('number is here {}'.format(number))

        if number < 0:
            raise NegativeNumberException(error_code=FactorialExecutionError.NEGATIVE_NUMBER)


class AckermannNumberValidator(ValidatorBase):

    def validate(self):

        n = self.context.n
        m = self.context.m

        if n < 0 or m < 0:
            raise NegativeNumberException(error_code=AckermannExecutionError.NEGATIVE_NUMBER)