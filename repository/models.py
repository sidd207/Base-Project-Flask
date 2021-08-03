class FibonacciModel:
    def __init__(self, number):
        self.number = number


    def to_dict(self):
        return {
            'number': self.number
        }


class FactoriallModel:
    def __init__(self, factorial_number):
        self.factorial_number = factorial_number


    def to_dict(self):
        return {
            'factorial_number': self.factorial_number
        }


class AckermannModel:
    def __init__(self, ackermann_value):
        self.ackermann_value = ackermann_value


    def to_dict(self):
        return {
            'ackermann_value': self.ackermann_value
        }