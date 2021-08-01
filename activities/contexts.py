class GenericContextBase(object):
    def __init__(self, **kwargs):
        self.set_context(**kwargs)

    def set_context(self, **attrs):
        """Set attribute values in context.

        Args:
        attrs: dict of attribute names and values.
        """
        for name, value in attrs.items():
            setattr(self, name, value)


class FibonacciContext(object):
    """
    context class for getting Fibonacci number
    """

    def __init__(self, number, **kwargs):
        self.number = number


class FactorialContext(object):
    """
    context class for getting factorial
    """

    def __init__(self, factorial_number, **kwargs):
        self.factorial_number = factorial_number


class AckermannContext(object):
    """
    context class for getting ackermann value of m and n
    """

    def __init__(self, n, m, **kwargs):
        self.n = n
        self.m = m