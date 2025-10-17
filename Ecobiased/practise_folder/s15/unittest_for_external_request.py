import unittest
from unittest.mock import patch
import requests


def fetch_data_from_api(url):
    response = requests.get(url)
    if response == 200:
        return response.json()
    else:
        return response.raise_for_status()


class TestFetchAPI(unittest.TestCase):

    def test_data_from_fetch_api_success(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'key': 'value'}
        mock_get.return_value = mock_response

        # call the function

        result = fetch_data_from_api('https://google.com')
        self.assertEqual(result, {'key': 'value'})
        mock_get.assert_called_once_with('https://google.com')

    def test_data_from_fetch_api_failure(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError('Not found')
        mock_get.return_value = mock_response

        # call the function and expect the expectations

        with self.assertRaises(requests.exceptions.HTTPError):
            fetch_data_from_api('https://google.com')
            mock_get.assert_called_once_with('https://google.com')


if __name__ == '__main__':
    unittest.main()