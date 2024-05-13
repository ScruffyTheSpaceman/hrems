"""HTTP Client tests"""
import unittest
from unittest import mock
import httpx
from app.utils import async_request


class TestAsyncClient(unittest.IsolatedAsyncioTestCase):
    """Test Async Client"""

    @mock.patch("httpx.AsyncClient.request", new_callable=mock.AsyncMock)
    async def test_successful_request(self, mock_request):
        """Test a successful request without retrying"""
        mock_request.return_value = "Success"

        client = async_request.get_client()
        response = await client.request("GET", "https://example.com")

        mock_request.assert_called_once_with("GET", "https://example.com")
        self.assertEqual(
            response,
            "Success",
            "The response should be \"Success\" for a successful request."
        )

    @mock.patch("httpx.AsyncClient.request", new_callable=mock.AsyncMock)
    async def test_retries_on_failure(self, mock_request):
        """Test that the client retries the specified number of times on failure"""
        mock_request.side_effect = [
            httpx.RequestError("Error"),
            httpx.RequestError("Error"),
            "Success"
        ]

        client = async_request.get_client()
        response = await client.request("GET", "https://example.com")

        self.assertEqual(
            mock_request.call_count, async_request.NUMBER_OF_RETRIES,
            f"The client should retry {async_request.NUMBER_OF_RETRIES} times."
        )
        self.assertEqual(
            response,
            "Success",
            "The response should be \"Success\" after retries."
        )

    @mock.patch("httpx.AsyncClient.request", new_callable=mock.AsyncMock)
    async def test_failure_after_max_retries(self, mock_request):
        """
        Test that the client raises a tenacity.RetryError after the maximum number of retries.
        """
        mock_request.side_effect = httpx.RequestError("Error")

        client = async_request.get_client()
        with self.assertRaises(async_request.tenacity.RetryError):
            await client.request("GET", "https://example.com")

        self.assertEqual(
            mock_request.call_count,
            async_request.NUMBER_OF_RETRIES,
            f"The client should stop retrying after {async_request.NUMBER_OF_RETRIES} attempts.")


if __name__ == "__main__":
    unittest.main()
