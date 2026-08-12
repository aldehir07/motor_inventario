from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies.auth import get_current_user
from app.api.dependencies.usuarios import (
    get_auth_service,
)
from app.api.schemas.api_response import ApiResponse
from app.api.schemas.auth_login_request import AuthLoginRequest
from app.api.schemas.token_response import TokenResponse
from app.api.schemas.usuario_response import UsuarioResponse
from app.api.utils.responses import success_response
from app.modules.usuarios.models.usuario import Usuario
from app.modules.usuarios.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"],
)


@router.post(
    "/login",
    response_model=ApiResponse[TokenResponse],
    status_code=status.HTTP_200_OK,
    summary="Iniciar sesión",
    description="Autentica un usuario y devuelve un token JWT de acceso.",
)
def login(
    request: AuthLoginRequest,
    service: Annotated[
        AuthService,
        Depends(get_auth_service),
    ],
):

    usuario, token = service.autenticar(
        request.email,
        request.password,
    )

    data = TokenResponse(
        access_token=token,
        usuario=UsuarioResponse.model_validate(usuario),
    )

    return success_response(
        data,
        "Autenticación exitosa.",
    )


@router.get(
    "/me",
    response_model=ApiResponse[UsuarioResponse],
    status_code=status.HTTP_200_OK,
    summary="Usuario autenticado",
    description="Devuelve la información del usuario autenticado.",
)
def obtener_usuario_actual(
    usuario: Annotated[
        Usuario,
        Depends(get_current_user),
    ],
):

    return success_response(
        UsuarioResponse.model_validate(usuario),
        "Usuario autenticado obtenido correctamente.",
    )