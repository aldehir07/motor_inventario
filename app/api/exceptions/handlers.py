from fastapi import Request
from fastapi.responses import JSONResponse

from app.shared.exceptions.not_found_exception import (
    NotFoundException,
)

from app.shared.exceptions.duplicate_exception import (
    DuplicateException,
)


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):

    return JSONResponse(

        status_code=500,

        content={

            "success": False,

            "error": "Internal Server Error",

            "message": str(exc),

        },

    )


async def not_found_exception_handler(
    request: Request,
    exc: NotFoundException,
):

    return JSONResponse(

        status_code=404,

        content={

            "success": False,

            "error": "Not Found",

            "message": str(exc),

        },

    )


async def duplicate_exception_handler(
    request: Request,
    exc: DuplicateException,
):

    return JSONResponse(

        status_code=409,

        content={

            "success": False,

            "error": "Duplicate",

            "message": str(exc),

        },

    )