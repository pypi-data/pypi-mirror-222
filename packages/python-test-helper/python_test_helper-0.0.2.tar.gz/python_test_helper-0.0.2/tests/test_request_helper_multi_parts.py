import unittest

from helper_methods.helper.request_helper import RequestHelper


class BasicTest(unittest.TestCase):

    def test_basic_https(self):
        sh = RequestHelper("https://jsonplaceholder.typicode.com/todos")

        response = sh.get("1")

        assert response.json()['id'] == 1


if __name__ == '__main__':
    unittest.main()
