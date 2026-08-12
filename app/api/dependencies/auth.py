from collections.abc import Callable
from typing import Annotated

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.api.dependencies.usuarios import get_auth_service
from app.modules.usuarios.enums.rol_usuario import RolUsuario
from app.modules.usuarios.exceptions.acceso_denegado_exception import (
    AccesoDenegadoException,
)
from app.modules.usuarios.exceptions.token_invalido_exception import (
    TokenInvalidoException,
)
from app.modules.usuarios.models.usuario import Usuario
from app.modules.usuarios.services.auth_service import AuthService
from app.modules.usuarios.services.token_service import TokenService

_bearer = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(_bearer),
    ],
    auth_service: Annotated[
        AuthService,
        Depends(get_auth_service),
    ],
) -> Usuario:

    if not credentials:
        raise TokenInvalidoException(
            "Se requiere un token de acceso."
        )

    token_service = TokenService()
    payload = token_service.decodificar_token(
        credentials.credentials
    )

    usuario_id = int(payload.get("sub"))

    return auth_service.obtener_usuario_por_token(
        usuario_id
    )


def require_roles(
    roles: set[RolUsuario],
) -> Callable[[Usuario], Usuario]:

    def _rol_dependency(
        usuario: Annotated[
            Usuario,
            Depends(get_current_user),
        ],
    ) -> Usuario:

        if usuario.rol not in roles:
            raise AccesoDenegadoException(
                "No tienes permisos para realizar esta operación."
            )

        return usuario

    return _rol_dependency