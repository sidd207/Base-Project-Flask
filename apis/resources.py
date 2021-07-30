import os
from flask import request
from flask_restx import Resource

from logs import logger

from utils import parse_response
from . import api
from .request_schema import FibonacciNumberSchema

ENV = os.environ['FLASK_ENV']
if not ENV:
    os.environ["FLASK_ENV"] = 'qa'


class FibonacciNumber(Resource):

    # @parse_response()
    @api.except(FibonacciNumberSchema.GET_FIBO_NUMBER)
    def get(self):
        print('working fine')
        response = {'one':'two'}
        return response


class AckermannFunction(Resource):

    # @parse_response()
    def get(self):
        pass

class Factorial(Resource):

    # @parse_response()
    def get(self):
        pass




