import requests
import unittest
from unittest.mock import patch


def fetch_data_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return response.raise_for_status()


class TestFetchDataFromAPI(unittest.TestCase):

    def test_fetch_data_from_api_success(self, mock_get):
        # mock the response object with the desired attributes.
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_response

        # call the function
        result = fetch_data_from_api('http://google.com')

        # assert the expected result
        self.assertEqual(result, {'key': 'value'})
        mock_get.assert_called_once_with('http://google.com')

    def test_fetch_data_from_api_failure(self, mock_get):
        # mock a response with an error status code
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Not Fount")
        mock_get.return_value = mock_response

        # call the function and expect and exception
        with self.assertRaises(requests.exceptions.HTTPError):
            fetch_data_from_api('http://google.com')

        mock_get.assert_called_once_with('http://google.com')


if __name__=='__main__':
    unittest.main()