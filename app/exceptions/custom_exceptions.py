"""Exception class is for working with common exceptions, to give better
error logs and tracking.
"""

from starlette.requests import Request
from starlette.responses import JSONResponse


ALREADY_EXISTS_EXCEPTION: str = "409"
PERMISSION_DENIED_EXCEPTION: str = "PermissionDenied"
RESOURCE_NOT_FOUND_EXCEPTION: str = "NotFound"

class ResourceNotFoundException(Exception):
    pass

class AlreadyExistsException(Exception):
    pass

class PermissionDeniedException(Exception):
    pass

async def resource_not_found_exception_handler(
    _: Request, exc: ResourceNotFoundException):
    """Handles the ResourceNotFoundException

    Args:
        request (Request): The incoming request.
        exc (ResourceNotFoundException): The raised ResourceNotFoundException.

    Returns:
        JSONResponse: The JSON response with a 404 status code and an error message.
    """
    return JSONResponse(status_code=404, content={
        "message": f"resource not found exception {str(exc)}"})


async def already_exists_exception_handler(_: Request, exc: AlreadyExistsException):
    """Handles the AlreadyExistsException.

    Args:
        request (Request): The incoming request.
        exc (AlreadyExistsException): The raised AlreadyExistsException.

    Returns:
        JSONResponse: The JSON response with a 409 status code and an error message.
    """
    return JSONResponse(status_code=409, content={
        "message": f"already exists exception {str(exc)}"})

async def permission_denied_exception_handler(_: Request, exc: AlreadyExistsException):
    """
    Handles the PermissionDeniedException.

    Args:
        request (Request): The incoming request.
        exc (PermissionDeniedException): The raised PermissionDeniedException.

    Returns:
        JSONResponse: The JSON response with a 403 status code and an error message.
    """
    return JSONResponse(status_code=403, content={
        "message": f"already exists exception {str(exc)}"})


def get_exception_handlers() -> dict:
    """Returns a dictionary of exception handlers.

    Returns:
        A dictionary of exception handlers.
    """
    return {
        ResourceNotFoundException: resource_not_found_exception_handler,
        AlreadyExistsException: already_exists_exception_handler,
        PermissionDeniedException: permission_denied_exception_handler
    }
