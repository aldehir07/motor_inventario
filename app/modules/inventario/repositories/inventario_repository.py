from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.inventario.models.inventario import Inventario
from app.shared.repositories.base_repository import BaseRepository
from app.modules.catalogo.models.producto import Producto


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

    def get_stock_bajo(self) -> list[Inventario]:

        stmt = (
            select(Inventario)
            .join(Inventario.producto)
            .where(
                Inventario.stock_actual <= Producto.stock_minimo
            )
            .order_by(
                Inventario.stock_actual.asc()
            )
        )

        return list(
            self.session.scalars(stmt)
        )

    def get_sin_stock(self) -> list[Inventario]:
        stmt = (
            select(Inventario)
            .join(Inventario.producto)
            .where(
                Inventario.stock_actual == 0
            )
            .order_by(
                Producto.nombre
            )
        )

        return list(
            self.session.scalars(stmt)
        )

    def get_valor_inventario(self) -> list[Inventario]:
        stmt = (
            select(Inventario)
            .join(Inventario.producto)
            .where(
                Producto.activo == True
            )
            .order_by(
                Producto.nombre
            )
        )

        return list(
            self.session.scalars(stmt)
        )