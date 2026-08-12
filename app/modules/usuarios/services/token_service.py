from datetime import datetime, timedelta, timezone

import jwt

from app.config.settings import settings
from app.modules.usuarios.enums.rol_usuario import RolUsuario
from app.modules.usuarios.exceptions.token_invalido_exception import (
    TokenInvalidoException,
)


class TokenService:

    def crear_token(
        self,
        usuario_id: int,
        rol: RolUsuario,
    ) -> str:

        expira = datetime.now(timezone.utc) + timedelta(
            minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
        )

        payload = {
            "sub": str(usuario_id),
            "rol": rol.value,
            "exp": expira,
        }

        return jwt.encode(
            payload,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM,
        )

    def decodificar_token(self, token: str) -> dict:

        try:
            return jwt.decode(
                token,
                settings.JWT_SECRET_KEY,
                algorithms=[settings.JWT_ALGORITHM],
            )
        except jwt.InvalidTokenError as exc:
            raise TokenInvalidoException(
                "El token no es válido o ha expirado."
            ) from exc