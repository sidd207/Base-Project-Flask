from flask_restx import fields, reqparse, inputs
from flask_restx._http import HTTPStatus
from flask_restx.errors import abort
from flask_restx.model import ModelBase, RE_REQUIRED
from jsonschema import Draft4Validator
from jsonschema import ValidationError


from apis import api
from constants import USER_UUID_HEADER, REQUEST_ID_HEADER
from errors import PayloadValidationErrorCodes

REGEX = r'^[1-9]\d*$/'


def validate(self, data, resolver=None, format_checker=None):
    validator = Draft4Validator(self.__schema__, resolver=resolver, format_checker=format_checker)

    try:
        validator.validate(data)
    except ValidationError:
        abort(HTTPStatus.BAD_REQUEST,
              success=False,
              data=[],
              _metadata='Input payload validation failed',
              errors=list(format_error(e) for e in validator.iter_errors(data))
              )


def format_error(error):
    path = list(error.path)
    if error.validator == 'required':
        name = RE_REQUIRED.match(error.message).group('name')
        path.append(name)
    field = '.'.join(str(p) for p in path)
    validator = error.validator
    value = error.validator_value
    error_data = PayloadValidationErrorCodes[validator].value
    error_message = error_data['error_message'].format(**{
        'field': field,
        'value': value
    })
    error_code = error_data['error_code']
    return {
        'error_code': error_code,
        'error_message': error_message
    }


ModelBase.validate = validate


class HeaderMap:
    USER_MAP = reqparse.RequestParser()
    USER_MAP.add_argument(USER_UUID_HEADER, type=str, required=True, location='headers', help="User's UUID")
    USER_MAP.add_argument(REQUEST_ID_HEADER, type=str, required=True, location='headers', help="Request UUID")


class FibonacciNumberSchema(object):

    fibonacci_parser = reqparse.RequestParser()
    fibonacci_parser.add_argument('number', type=int, required=True)


class FactorialNumberSchema(object):

    factorial_parser = reqparse.RequestParser()
    factorial_parser.add_argument('factorial_number', type=int, required=True)


class AckermannSchema(object):

    ackermann_parser = reqparse.RequestParser()
    ackermann_parser.add_argument('n', type=int, required=True)
    ackermann_parser.add_argument('m', type=int, required=True)