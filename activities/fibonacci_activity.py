from activities.base import ActivityBase
from activities.contexts import FibonacciContext
from activities.validators.validators import FibonacciNumberValidator
from errors import FibonacciExecutionError
from exceptions import FibonacciCalculationException
from commons.errors import Error

from logs import logger
from repository.models import FibonacciModel


class FibonacciActivity(ActivityBase):
    """
    Fibonacci series number calculation activity class
    """

    context_class = FibonacciContext

    payload_validators = (
        FibonacciNumberValidator,
    )

    def _execute(self):

        error_code =None
        exception_obj = None
        error_message = ''

        try:
            fib_number = self.fibonacci_calculation()
            response = FibonacciModel(**fib_number)
            self.response.data.append(response)
            self.response.success = True
            self.response.message = "Sucessfully calcualted given position of fibonacci series: "\
                                    +str(self.context.number)
        except FibonacciCalculationException as e:
            logger.info('Exception occurs while trying to calculate fibanocci number {}'.format(e))
            error_code = FibonacciExecutionError.FIBONACCI_RUNTIME_ERROR
            exception_obj = e

        if error_code:
            self.response.errors.append(Error(error_code.name, error_code.value))
            logger.error(exception_obj)


    def fibonacci_calculation(self):

        number = self.context.number

        first = 0
        second = 1

        if number == 0:
            return {'number': first}
        elif number == 1:
            return {'number': second}
        else:
            for i in range(2, number + 1):
                temp = first + second
                first = second
                second = temp
            return {'number': second}
