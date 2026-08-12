from sqlalchemy.orm import Session

from app.config.logger import logger
from app.modules.usuarios.models.usuario import Usuario
from app.modules.usuarios.repositories.usuario_repository import (
    UsuarioRepository,
)
from app.modules.usuarios.schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioUpdate,
)
from app.modules.usuarios.value_objects.password import Password
from app.shared.exceptions.duplicate_exception import DuplicateException
from app.shared.exceptions.not_found_exception import NotFoundException


class UsuarioService:

    def __init__(self, session: Session):
        self.session = session
        self.repository = UsuarioRepository(session)

    def crear_usuario(self, data: UsuarioCreate) -> Usuario:

        logger.info("Iniciando creación del usuario '{}'", data.email)

        if self.repository.get_by_email(data.email):
            raise DuplicateException(
                f"Ya existe un usuario con el email '{data.email}'."
            )

        usuario = Usuario(
            nombre_completo=data.nombre_completo,
            email=data.email,
            password_hash=Password.hash(data.password),
            rol=data.rol,
        )

        self.repository.add(usuario)
        logger.info(
            "Guardando usuario '{}' en la base de datos",
            data.email,
        )
        self.session.commit()
        self.session.refresh(usuario)

        logger.success(
            "Usuario '{}' creado correctamente con ID {}",
            usuario.email,
            usuario.id,
        )
        return usuario

    def listar_usuarios(self) -> list[Usuario]:
        return self.repository.get_all()

    def obtener_usuario(self, usuario_id: int) -> Usuario:

        usuario = self.repository.get_by_id(usuario_id)

        if not usuario:
            raise NotFoundException(
                f"No existe el usuario con ID {usuario_id}"
            )

        return usuario

    def actualizar_usuario(
        self,
        usuario_id: int,
        data: UsuarioUpdate,
    ) -> Usuario:

        usuario = self.repository.get_by_id(usuario_id)

        if not usuario:
            raise NotFoundException(
                f"No existe el usuario con ID {usuario_id}"
            )

        cambios = data.model_dump(exclude_unset=True)

        email = cambios.get("email")
        if email and email != usuario.email:
            if self.repository.get_by_email(email):
                raise DuplicateException(
                    f"Ya existe un usuario con el email '{email}'."
                )

        password = cambios.pop("password", None)
        if password:
            cambios["password_hash"] = Password.hash(password)

        for campo, valor in cambios.items():
            setattr(usuario, campo, valor)

        logger.info("Actualizando usuario ID {}", usuario_id)
        self.session.commit()
        self.session.refresh(usuario)

        logger.success(
            "Usuario '{}' actualizado correctamente",
            usuario.email,
        )
        return usuario

    def desactivar_usuario(self, usuario_id: int) -> Usuario:

        usuario = self.repository.get_by_id(usuario_id)

        if not usuario:
            raise NotFoundException(
                f"No existe el usuario con ID {usuario_id}"
            )

        usuario.activo = False

        logger.warning("Desactivando usuario '{}'", usuario.email)
        self.session.commit()
        self.session.refresh(usuario)

        logger.success(
            "Usuario '{}' desactivado correctamente",
            usuario.email,
        )
        return usuario