from fastapi import Request
from fastapi.responses import JSONResponse


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    """
    Maneja cualquier excepción no controlada.
    """

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal Server Error",
            "message": str(exc),
        },
    )