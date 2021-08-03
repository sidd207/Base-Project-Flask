from activities.base import ActivityBase
from activities.contexts import FactorialContext
from activities.validators.validators import FactorialNumberValidator
from errors import FactorialExecutionError
from exceptions import FactorialCalculationException
from commons.errors import Error

from logs import logger
from repository.models import FactoriallModel


class FactorialActivity(ActivityBase):
    """
    Factorial calculation of a given number activity class
    """

    context_class = FactorialContext

    payload_validators = (
        FactorialNumberValidator,
    )

    def _execute(self):

        error_code =None
        exception_obj = None
        error_message = ''

        try:
            fac_number = self.factorial_calculation()
            response = FactoriallModel(**fac_number)
            self.response.data.append(response)
            self.response.success = True
            self.response.message = "Sucessfully calcualted factorial of given number: " \
                                    +str(self.context.factorial_number)
        except FactorialCalculationException as e:
            logger.info('Exception occurs while trying to calculate factorial of a number {}'.format(e))
            error_code = FactorialExecutionError.FIBONACCI_RUNTIME_ERROR
            exception_obj = e

        if error_code:
            self.response.errors.append(Error(error_code.name, error_code.value))
            logger.error(exception_obj)


    def factorial_calculation(self):

        n = self.context.factorial_number
        result = 1

        for i in range(2, n+1):
            result *= i

        return {
            'factorial_number': result
        }





