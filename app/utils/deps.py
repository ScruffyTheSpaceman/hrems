"""Deps variables to access Azure Cloud Storage"""

from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
from app.core import config


api_key_header = APIKeyHeader(
    name=config.Settings().API_KEY_NAME,
    auto_error=False,
    scheme_name="API Key Header")


async def get_api_key(
    api_key_header: str = Security(api_key_header)):  # pylint: disable=redefined-outer-name
    """Returns the Cloud Storage API key if avalible.

    Args:
        api_key_query: Value of API key within query params.
        api_key_query: Value of API key within header.

    Returns:
      API key value.

    Raises:
        HTTPException is API key is not found.
    """

    if api_key_header == config.Settings().API_KEY:
        return api_key_header
    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN,
        detail="Could not validate credentials")
