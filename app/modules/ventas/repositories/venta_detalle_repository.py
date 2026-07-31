from sqlalchemy.orm import Session

from sqlalchemy import func, select

from app.modules.catalogo.models.producto import Producto
from app.modules.ventas.models.venta import Venta
from app.modules.ventas.models.venta_detalle import VentaDetalle
from app.modules.ventas.enums.estado_venta import EstadoVenta
from app.shared.repositories.base_repository import BaseRepository


class VentaDetalleRepository(BaseRepository[VentaDetalle]):

    def __init__(self, session: Session):
        super().__init__(
            session,
            VentaDetalle,
        )

    def get_productos_mas_vendidos(self,):

        stmt = (
            select(
                Producto.id,
                Producto.codigo,
                Producto.nombre,
                func.sum(
                    VentaDetalle.cantidad
                ).label("cantidad_vendida"),
            )
            .join(VentaDetalle.producto)
            .join(VentaDetalle.venta)
            .where(
                Venta.estado == EstadoVenta.CONFIRMADA
            )
            .group_by(
                Producto.id,
                Producto.codigo,
                Producto.nombre,
            )

            .order_by(
                func.sum(
                    VentaDetalle.cantidad
                ).desc()
            )
        )

        return self.session.execute(stmt).all()