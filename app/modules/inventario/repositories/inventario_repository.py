from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.inventario.models.inventario import Inventario
from app.shared.repositories.base_repository import BaseRepository


class InventarioRepository(BaseRepository[Inventario]):

    def __init__(self, session: Session):
        super().__init__(session, Inventario)

    def get_by_producto_id(
        self,
        producto_id: int,
    ) -> Inventario | None:

        stmt = (
            select(Inventario)
            .where(Inventario.producto_id == producto_id)
        )

        return self.session.scalar(stmt)