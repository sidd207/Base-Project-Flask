from tests.base import BaseTestCase
from config.base import DEFAULT_USER_UUID, DEFAULT_REQUEST_ID
import json


class AckermannApiTestCases(BaseTestCase):
    """
    Test cases for ackermann function api.
    """

    def test_successful_fibonacci_api_test(self):
        headers ={
            'User-Uuid' : DEFAULT_USER_UUID,
            'Request-Id' : DEFAULT_REQUEST_ID
        }
        params = {
            'm': 2,
            'n': 3
        }

        response = self.app.get('/api/v1/ackermann', headers=headers,  query_string=params)
        response_dict = json.loads(response.data)
        ackermann_value = response_dict['data'][0]['ackermann_value']

        self.assertEqual(9, ackermann_value)
        self.assertEqual(200, response.status_code)

    def test_invalid_fibonacci_number(self):
        headers = {
            'User-Uuid': DEFAULT_USER_UUID,
            'Request-Id': DEFAULT_REQUEST_ID
        }
        params = {
            'm': -2,
            'n': -3
        }

        response = self.app.get('/api/v1/ackermann', headers=headers, query_string=params)
        self.assertEqual(400, response.status_code)

    def test_insufficient_params(self):
        headers = {
            'User-Uuid': DEFAULT_USER_UUID,
            'Request-Id': DEFAULT_REQUEST_ID
        }
        params = {}

        response = self.app.get('/api/v1/ackermann', headers=headers, query_string=params)
        self.assertEqual(400, response.status_code)

    def test_invalid_url(self):
        headers = {
            'User-Uuid': DEFAULT_USER_UUID,
            'Request-Id': DEFAULT_REQUEST_ID
        }
        params = {
            'm': 2,
            'n': 3
        }

        response = self.app.get('/api/v1/ackermann/', headers=headers, query_string=params)

        self.assertEqual(404, response.status_code)


