import unittest
from app import app


class BaseTestCase(unittest.TestCase):
    """
    Test cases to check whether apis are working fine or not.
    """

    # def create_app(self):
    #     app.config.from_object('config.testing')
    #     return app.test_client()

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass