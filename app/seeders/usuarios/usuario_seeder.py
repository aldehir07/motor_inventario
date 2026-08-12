from app.config.logger import logger
from app.config.settings import settings
from app.modules.usuarios.enums.rol_usuario import RolUsuario
from app.modules.usuarios.models.usuario import Usuario
from app.modules.usuarios.repositories.usuario_repository import (
    UsuarioRepository,
)
from app.modules.usuarios.value_objects.password import Password
from app.seeders.base_seeder import BaseSeeder


class UsuarioSeeder(BaseSeeder):

    def __init__(self, session):
        super().__init__(session)
        self.repository = UsuarioRepository(session)

    def run(self) -> None:

        if not settings.ADMIN_EMAIL or not settings.ADMIN_PASSWORD:
            raise ValueError(
                "ADMIN_EMAIL y ADMIN_PASSWORD son requeridos "
                "para crear el usuario administrador."
            )

        if self.repository.get_by_email(settings.ADMIN_EMAIL):
            logger.info(
                "El usuario administrador '{}' ya existe",
                settings.ADMIN_EMAIL,
            )
            return

        admin = Usuario(
            nombre_completo="Administrador del Sistema",
            email=settings.ADMIN_EMAIL,
            password_hash=Password.hash(settings.ADMIN_PASSWORD),
            rol=RolUsuario.ADMIN,
        )

        self.add(admin)
        self.commit()

        logger.success(
            "Usuario administrador '{}' creado correctamente",
            admin.email,
        )