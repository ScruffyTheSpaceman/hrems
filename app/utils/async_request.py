"""This module contains helper function to create AsyncClient instance"""""

import httpx
import tenacity

NUMBER_OF_RETRIES: int = 3

class RetryingClient(httpx.AsyncClient):
    """A subclass of httpx.AsyncClient that implements automatic retry."""
    async def request(self, *args, **kwargs):
        """Override the request method to implement retry logic.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            httpx.Response: An instance of httpx.Response.
        """
        async for attempt in tenacity.AsyncRetrying(
            retry=tenacity.retry_if_exception_type(httpx.RequestError),
            stop=tenacity.stop_after_attempt(NUMBER_OF_RETRIES),
            wait=tenacity.wait_exponential()):
            with attempt:
                return await super().request(*args, **kwargs)

def get_client():
    """Function to get an instance of RetryingClient.

    Returns:
        RetryingClient: An instance of RetryingClient.
    """
    return RetryingClient()
