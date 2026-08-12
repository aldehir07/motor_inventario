from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.usuarios.services.auth_service import AuthService
from app.modules.usuarios.services.usuario_service import UsuarioService


def get_auth_service(
    db: Annotated[
        Session,
        Depends(get_db),
    ],
) -> AuthService:

    return AuthService(db)


def get_usuario_service(
    db: Annotated[
        Session,
        Depends(get_db),
    ],
) -> UsuarioService:

    return UsuarioService(db)