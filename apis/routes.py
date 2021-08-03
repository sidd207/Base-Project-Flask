"""
    This module is responsible for adding resouces of the APIs to the blueprint.
"""

from . import api, resources


api.add_resource(resources.FibonacciNumber, '/fibonacci', endpoint='fibonacci')
api.add_resource(resources.AckermannFunction, '/ackermann', endpoint='ackermann')
api.add_resource(resources.Factorial, '/factorial', endpoint='factorial')

