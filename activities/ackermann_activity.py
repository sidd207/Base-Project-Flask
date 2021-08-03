from activities.base import ActivityBase
from activities.contexts import AckermannContext
from activities.validators.validators import AckermannNumberValidator
from errors import AckermannExecutionError
from exceptions import AckermannCalculationException
from commons.errors import Error

from logs import logger
from repository.models import AckermannModel


class AckermannlActivity(ActivityBase):
    """
    Ackermann Function activity class
    """

    context_class = AckermannContext

    payload_validators = (
        AckermannNumberValidator,
    )

    def _execute(self):

        error_code =None
        exception_obj = None
        error_message = ''

        try:
            fac_number = self.ackermann_calculation()
            response = AckermannModel(**fac_number)
            self.response.data.append(response)
            self.response.success = True
            self.response.message = "Sucessfully calcualted ackermann function of given numbers"
        except AckermannCalculationException as e:
            logger.info('Exception occurs while trying to calculate ackermann value of given numbers {}'.format(e))
            error_code = AckermannExecutionError.ACKERMANN_RUNTIME_ERROR
            exception_obj = e

        if error_code:
            self.response.errors.append(Error(error_code.name, error_code.value))
            logger.error(exception_obj)


    def ackermann_calculation(self):

        n = self.context.n
        m = self.context.m

        result = self.ackermann(m, n)
        return {
            'ackermann_value': result
        }

    def ackermann(self, m, n):

        if m == 0:
            return n + 1
        if n == 0:
            return self.ackermann(m - 1, 1)
        n2 = self.ackermann(m, n - 1)
        return self.ackermann(m - 1, n2)




