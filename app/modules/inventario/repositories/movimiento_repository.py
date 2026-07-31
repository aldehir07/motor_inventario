from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.inventario.models.movimiento_inventario import MovimientoInventario
from app.shared.repositories.base_repository import BaseRepository


class MovimientoRepository(BaseRepository[MovimientoInventario]):

    def __init__(self, session: Session):
        super().__init__(session, MovimientoInventario)

    def historial_producto(
        self,
        inventario_id: int,
    ) -> list[MovimientoInventario]:

        stmt = (
            select(MovimientoInventario)
            .where(
                MovimientoInventario.inventario_id == inventario_id
            )
            .order_by(
                MovimientoInventario.fecha_creacion.desc()
            )
        )

        return list(self.session.scalars(stmt))

    def get_kardax(self, producto_id: int) -> list[MovimientoInventario]:
        stmt = (
            select(MovimientoInventario)
            .join(
                MovimientoInventario.inventario
            )
            .where(
                MovimientoInventario.inventario.has(
                    producto_id=producto_id
                )
            )
            .order_by(
                MovimientoInventario.fecha_creacion
            )
        )
        return list(self.session.scalars(stmt))