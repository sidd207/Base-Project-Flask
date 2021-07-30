from flask_restx import fields, reqparse, inputs
from flask_restx._http import HTTPStatus
from flask_restx.errors import abort
from flask_restx.model import ModelBase, RE_REQUIRED
from jsonschema import Draft4Validator
from jsonschema import ValidationError


from apis import api
from errors import PayloadValidationErrorCodes



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

class FibonacciNumberSchema(object):

    GET_FIBO_NUMBER = api.model('FibonacciNumber', {
        'one' : fields.String(description='testing description', required=True)
    })