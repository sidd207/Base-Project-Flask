import os
from flask import request
from flask_restx import Resource

from activities.ackermann_activity import AckermannlActivity
from activities.factorial_activity import FactorialActivity
from activities.fibonacci_activity import FibonacciActivity
from logs import logger

from utils import parse_response
from . import api
from .request_schema import FibonacciNumberSchema, HeaderMap, FactorialNumberSchema, AckermannSchema
from constants import USER_UUID_HEADER, REQUEST_ID_HEADER
import json

ENV = os.environ['FLASK_ENV']
if not ENV:
    os.environ["FLASK_ENV"] = 'qa'


@api.doc(parser=HeaderMap.USER_MAP)
class FibonacciNumber(Resource):

    @api.expect(FibonacciNumberSchema.fibonacci_parser, validate=True)
    @parse_response()
    def get(self):
        payload = FibonacciNumberSchema.fibonacci_parser.parse_args()
        headers = HeaderMap.USER_MAP.parse_args()
        user_uuid = headers.get(USER_UUID_HEADER)
        request_id = headers.get(REQUEST_ID_HEADER)
        response = FibonacciActivity(user_uuid, request_id).execute(payload)
        logger.info(response.message)
        return response


@api.doc(parser=HeaderMap.USER_MAP)
class Factorial(Resource):

    @api.expect(FactorialNumberSchema.factorial_parser, validate=True)
    @parse_response()
    def get(self):
        payload = FactorialNumberSchema.factorial_parser.parse_args()
        headers = HeaderMap.USER_MAP.parse_args()
        user_uuid = headers.get(USER_UUID_HEADER)
        request_id = headers.get(REQUEST_ID_HEADER)
        response = FactorialActivity(user_uuid, request_id).execute(payload)
        logger.info(response.message)
        return response

@api.doc(parser=HeaderMap.USER_MAP)
class AckermannFunction(Resource):

    @api.expect(AckermannSchema.ackermann_parser, validate=True)
    @parse_response()
    def get(self):
        payload = AckermannSchema.ackermann_parser.parse_args()
        headers = HeaderMap.USER_MAP.parse_args()
        user_uuid = headers.get(USER_UUID_HEADER)
        request_id = headers.get(REQUEST_ID_HEADER)
        response = AckermannlActivity(user_uuid, request_id).execute(payload)
        logger.info(response.message)
        return response




