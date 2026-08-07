from typing import Any

from app.api.schemas.api_response import ApiResponse


def success_response(
    data: Any,
    message: str,
) -> ApiResponse:

    return ApiResponse(

        success=True,

        message=message,

        data=data,
    )