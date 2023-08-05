import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import warnings
import requests

from oapi2mockserver import expectation
from oapi2mockserver import requester


# ignores warnings
def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            test_func(self, *args, **kwargs)

    return do_test


""" Test for the requester class located in the main package """


class Test_Requester(unittest.TestCase):

    def setUp(self):
        self.mock_requester = requester.MockserverRequester()
        uri = 'localhost'
        self.mock_requester.set_mockserver_uri(uri)

    """ url change for mockserver uri is possible """

    def test_set_url(self):
        uri = 'google.com'
        self.mock_requester.set_mockserver_uri(uri)
        self.assertEqual(self.mock_requester.mockserver_uri, 'http://' + uri)

    """ test expectations method. It should clear existing expectations and put the new one into mockserver"""
    def test_expectations(self):
        test_expectation = expectation.Expectation()
        test_expectation.set_path("/v1/foo/bar")
        test_expectation.set_method("GET")
        test_expectation.set_status_code(200)
        path = test_expectation.get()['httpRequest']['path']
        method = test_expectation.get()['httpRequest']['method']
        response_mock = ResponseMock()
        response_data = [
            {
                'httpRequest': {
                    'path': path,
                    'method': method,
                }
            }
        ]
        response_mock.json = MagicMock(return_value=response_data)
        requests.put = MagicMock(return_value=response_mock)

        self.mock_requester.request_expectations([test_expectation])

        requests.put.assert_any_call(
            'http://localhost/mockserver/clear',
            data='{"path": "%s", "method": "%s"}' % (path, method)
        )
        requests.put.assert_any_call(
            'http://localhost/mockserver/expectation',
            data=test_expectation.get_json()
        )

    """ test reset method """

    @patch('oapi2mockserver.requester.requests.put', autospec=False)
    def test_reset(self, mock_requests):
        # check for success
        mock_requests.return_value.status_code = 200
        self.assertTrue(self.mock_requester.request_reset())
        # check for failure
        mock_requests.return_value.status_code = 404
        self.assertFalse(self.mock_requester.request_reset())


class ResponseMock(object):
    pass


if __name__ == '__main__':
    unittest.main()
