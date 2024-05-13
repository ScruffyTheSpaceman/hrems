"""Test custom exceptions."""
import unittest
from unittest import mock

from starlette import responses

from app.exceptions import custom_exceptions


class CustomExceptionsTest(unittest.IsolatedAsyncioTestCase):
    """Unit test cases for CustomExceptions."""

    async def test_resource_not_found_exception_handler(self):
        """Test the resource_not_found_exception_handler method."""
        request = mock.Mock()
        response = await custom_exceptions.resource_not_found_exception_handler(
            request, "exc")
        self.assertEqual(response.status_code, 404)

    async def test_already_exists_exception_handler(self):
        """Test the already_exists_exception_handler method."""
        request = mock.Mock()
        response = await custom_exceptions.already_exists_exception_handler(
            request, "exc")
        self.assertEqual(response.status_code, 409)

    async def test_permission_denied_exception_handler(self):
        """Test the permission_denied_exception_handler method."""
        request = mock.Mock()
        response = await custom_exceptions.permission_denied_exception_handler(
            request, "exc")
        self.assertEqual(response.status_code, 403)

    def test_get_exception_handlers(self):
        """Test the get_exception_handlers method."""
        mock_responses = responses
        mock_responses.JSONResponse = mock.AsyncMock(return_value="response")
        handlers = custom_exceptions.get_exception_handlers()
        expected_handlers = {
            custom_exceptions.ResourceNotFoundException: custom_exceptions.resource_not_found_exception_handler,  # pylint: disable=line-too-long
            custom_exceptions.AlreadyExistsException: custom_exceptions.already_exists_exception_handler,  # pylint: disable=line-too-long
            custom_exceptions.PermissionDeniedException: custom_exceptions.permission_denied_exception_handler  # pylint: disable=line-too-long
        }
        self.assertDictEqual(handlers, expected_handlers)


if __name__ == "__main__":
    unittest.main()


