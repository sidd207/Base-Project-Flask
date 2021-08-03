from tests.base import BaseTestCase
from config.base import DEFAULT_USER_UUID, DEFAULT_REQUEST_ID
import json


class FactorialApiTestCases(BaseTestCase):
    """
    Test cases for factorial calculation api.
    """

    def test_successful_factorial_calc_test(self):
        headers ={
            'User-Uuid' : DEFAULT_USER_UUID,
            'Request-Id' : DEFAULT_REQUEST_ID
        }
        params = {
            'factorial_number': 5
        }

        response = self.app.get('/api/v1/factorial', headers=headers,  query_string=params)
        response_dict = json.loads(response.data)
        factorial_number = response_dict['data'][0]['factorial_number']

        self.assertEqual(120, factorial_number)
        self.assertEqual(200, response.status_code)

    def test_invalid_factorial_number(self):
        headers = {
            'User-Uuid': DEFAULT_USER_UUID,
            'Request-Id': DEFAULT_REQUEST_ID
        }
        params = {
            'factorial_number': -5
        }

        response = self.app.get('/api/v1/factorial', headers=headers, query_string=params)
        self.assertEqual(400, response.status_code)

    def test_insufficient_params(self):
        headers = {
            'User-Uuid': DEFAULT_USER_UUID,
            'Request-Id': DEFAULT_REQUEST_ID
        }
        params = {}

        response = self.app.get('/api/v1/factorial', headers=headers, query_string=params)
        self.assertEqual(400, response.status_code)

    def test_invalid_url(self):
        headers = {
            'User-Uuid': DEFAULT_USER_UUID,
            'Request-Id': DEFAULT_REQUEST_ID
        }
        params = {
            'factorial_number': 5
        }

        response = self.app.get('/api/v1/factorial/', headers=headers, query_string=params)

        self.assertEqual(404, response.status_code)


