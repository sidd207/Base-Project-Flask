from tests.base import BaseTestCase
from config.base import DEFAULT_USER_UUID, DEFAULT_REQUEST_ID
import json


class FibonacciApiTestCases(BaseTestCase):
    """
    Test cases for fibonacci series number calculation api.
    """

    def test_successful_fibonacci_api_test(self):
        headers ={
            'User-Uuid' : DEFAULT_USER_UUID,
            'Request-Id' : DEFAULT_REQUEST_ID
        }
        params = {
            'number': 9
        }

        response = self.app.get('/api/v1/fibonacci', headers=headers,  query_string=params)
        response_dict = json.loads(response.data)
        number = response_dict['data'][0]['number']

        self.assertEqual(34, number)
        self.assertEqual(200, response.status_code)

    def test_invalid_fibonacci_number(self):
        headers = {
            'User-Uuid': DEFAULT_USER_UUID,
            'Request-Id': DEFAULT_REQUEST_ID
        }
        params = {
             'number': -5
        }

        response = self.app.get('/api/v1/fibonacci', headers=headers, query_string=params)
        self.assertEqual(400, response.status_code)

    def test_insufficient_params(self):
        headers = {
            'User-Uuid': DEFAULT_USER_UUID,
            'Request-Id': DEFAULT_REQUEST_ID
        }
        params = {}

        response = self.app.get('/api/v1/fibonacci', headers=headers, query_string=params)
        self.assertEqual(400, response.status_code)

    def test_invalid_url(self):
        headers = {
            'User-Uuid': DEFAULT_USER_UUID,
            'Request-Id': DEFAULT_REQUEST_ID
        }
        params = {
            'number': 5
        }

        response = self.app.get('/api/v1/fibonacci/', headers=headers, query_string=params)

        self.assertEqual(404, response.status_code)


