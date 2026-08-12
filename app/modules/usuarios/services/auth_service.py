from sqlalchemy.orm import Session

from app.config.logger import logger
from app.modules.usuarios.exceptions.credenciales_invalidas_exception import (
    CredencialesInvalidasException,
)
from app.modules.usuarios.exceptions.token_invalido_exception import (
    TokenInvalidoException,
)
from app.modules.usuarios.exceptions.usuario_inactivo_exception import (
    UsuarioInactivoException,
)
from app.modules.usuarios.models.usuario import Usuario
from app.modules.usuarios.repositories.usuario_repository import (
    UsuarioRepository,
)
from app.modules.usuarios.services.token_service import TokenService
from app.modules.usuarios.value_objects.password import Password


class AuthService:

    def __init__(self, session: Session):
        self.session = session
        self.repository = UsuarioRepository(session)
        self.token_service = TokenService()

    def autenticar(
        self,
        email: str,
        password: str,
    ) -> tuple[Usuario, str]:

        logger.info("Intento de autenticación para '{}'", email)

        usuario = self.repository.get_by_email(email)

        if not usuario or not Password.verify(
            password,
            usuario.password_hash,
        ):
            logger.warning(
                "Credenciales inválidas para '{}'",
                email,
            )
            raise CredencialesInvalidasException(
                "El email o la contraseña son incorrectos."
            )

        if not usuario.activo:
            logger.warning("Usuario '{}' inactivo", email)
            raise UsuarioInactivoException(
                "El usuario está inactivo."
            )

        token = self.token_service.crear_token(
            usuario.id,
            usuario.rol,
        )

        logger.success(
            "Autenticación exitosa para '{}'",
            email,
        )

        return usuario, token

    def obtener_usuario_por_token(
        self,
        usuario_id: int,
    ) -> Usuario:

        usuario = self.repository.get_by_id(usuario_id)

        if not usuario or not usuario.activo:
            raise TokenInvalidoException(
                "El usuario asociado al token no existe o está inactivo."
            )

        return usuario