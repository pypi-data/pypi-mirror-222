import unittest

from requests.exceptions import MissingSchema

from helper_methods.helper.request_helper import RequestHelper


class BasicTest(unittest.TestCase):

    def test_basic_https(self):
        sh = RequestHelper("https://jsonplaceholder.typicode.com/")

        response = sh.get("todos/1")

        assert response.json()['id'] == 1

    def test_basic_http(self):
        sh = RequestHelper("http://jsonplaceholder.typicode.com/")

        response = sh.get("todos/1")

        assert response.json()['id'] == 1

    def test_basic_unhappy(self):
        try:
            RequestHelper("jsonplaceholder.typicode.com/")
            raise AssertionError("Did not receive expected exception")
        except MissingSchema:
            pass


if __name__ == '__main__':
    unittest.main()
