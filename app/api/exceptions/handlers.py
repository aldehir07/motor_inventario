from fastapi import Request
from fastapi.responses import JSONResponse

from app.shared.exceptions.not_found_exception import (
    NotFoundException,
)

from app.shared.exceptions.duplicate_exception import (
    DuplicateException,
)
from app.shared.exceptions.conflict_exception import (
    ConflictException,
)

from app.modules.usuarios.exceptions.acceso_denegado_exception import (
    AccesoDenegadoException,
)
from app.modules.usuarios.exceptions.credenciales_invalidas_exception import (
    CredencialesInvalidasException,
)
from app.modules.usuarios.exceptions.token_invalido_exception import (
    TokenInvalidoException,
)
from app.modules.usuarios.exceptions.usuario_inactivo_exception import (
    UsuarioInactivoException,
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

async def conflict_exception_handler(
    request: Request,
    exc: ConflictException,
):
    return JSONResponse(
        status_code=409,
        content={
            "success": False,
            "error": "Conflict",
            "message": str(exc),
        },
    )


async def credenciales_invalidas_exception_handler(
    request: Request,
    exc: CredencialesInvalidasException,
):
    return JSONResponse(
        status_code=401,
        content={
            "success": False,
            "error": "Unauthorized",
            "message": str(exc),
        },
    )


async def token_invalido_exception_handler(
    request: Request,
    exc: TokenInvalidoException,
):
    return JSONResponse(
        status_code=401,
        content={
            "success": False,
            "error": "Unauthorized",
            "message": str(exc),
        },
    )


async def usuario_inactivo_exception_handler(
    request: Request,
    exc: UsuarioInactivoException,
):
    return JSONResponse(
        status_code=403,
        content={
            "success": False,
            "error": "Forbidden",
            "message": str(exc),
        },
    )


async def acceso_denegado_exception_handler(
    request: Request,
    exc: AccesoDenegadoException,
):
    return JSONResponse(
        status_code=403,
        content={
            "success": False,
            "error": "Forbidden",
            "message": str(exc),
        },
    )