from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.usuarios.models.usuario import Usuario
from app.shared.repositories.base_repository import BaseRepository


class UsuarioRepository(BaseRepository[Usuario]):

    def __init__(self, session: Session):
        super().__init__(session, Usuario)

    def get_by_email(self, email: str) -> Usuario | None:
        stmt = select(Usuario).where(Usuario.email == email)
        return self.session.scalar(stmt)

    def get_by_id(self, usuario_id: int) -> Usuario | None:
        return self.session.get(Usuario, usuario_id)