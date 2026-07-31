from sqlalchemy import func, select, extract
from sqlalchemy.orm import Session

from app.modules.catalogo.models.producto import Producto
from app.modules.compras.models.compra import Compra
from app.modules.compras.enums.estado_compra import EstadoCompra
from app.modules.inventario.models.inventario import Inventario

from app.modules.ventas.models.venta import Venta
from app.modules.ventas.enums.estado_venta import EstadoVenta
from app.modules.ventas.models.venta_detalle import VentaDetalle


class AnalyticsRepository:

    def __init__(self, session: Session):

        self.session = session

    def total_productos(self,) -> int:

        stmt = select(
            func.count(Producto.id)
        )

        return self.session.scalar(stmt) or 0

    def productos_activos(self,) -> int:

        stmt = (
            select(func.count(Producto.id))
                .where(Producto.activo == True)
        )

        return self.session.scalar(stmt) or 0

    def productos_sin_stock(self,) -> int:

        stmt = (select(func.count(Inventario.id))
                .where(
                    Inventario.stock_actual == 0
                    )
                )

        return self.session.scalar(stmt) or 0

    def total_compras(self,) -> int:

        stmt = select(func.count(Compra.id))

        return self.session.scalar(stmt) or 0

    def total_ventas(self,) -> int:

        stmt = select(func.count(Venta.id))

        return self.session.scalar(stmt) or 0

    def ventas_por_mes(
        self,
    ) -> list:

        stmt = (

            select(
                extract(
                    "year",
                    Venta.fecha,
                ).label("anio"),
                extract(
                    "month",
                    Venta.fecha,
                ).label("mes"),

                func.sum(
                    Venta.total
                ).label("total"),
            )
            .where(
                Venta.estado == EstadoVenta.CONFIRMADA
            )

            .group_by(

                extract(
                    "year",
                    Venta.fecha,
                ),

                extract(
                    "month",
                    Venta.fecha,
                ),

            )

            .order_by(

                extract(
                    "year",
                    Venta.fecha,
                ),

                extract(
                    "month",
                    Venta.fecha,
                ),

            )

        )

        return self.session.execute(stmt).all()

    def compras_por_mes(
        self,
    ) -> list:

        stmt = (

            select(

                extract(
                    "year",
                    Compra.fecha,
                ).label("anio"),

                extract(
                    "month",
                    Compra.fecha,
                ).label("mes"),

                func.sum(
                    Compra.total
                ).label("total"),

            )

            .where(
                Compra.estado == EstadoCompra.CONFIRMADA
            )

            .group_by(

                extract(
                    "year",
                    Compra.fecha,
                ),

                extract(
                    "month",
                    Compra.fecha,
                ),

            )

            .order_by(

                extract(
                    "year",
                    Compra.fecha,
                ),

                extract(
                    "month",
                    Compra.fecha,
                ),

            )

        )

        return self.session.execute(stmt).all()

    def rotacion_inventario(
        self,
    ):

        stmt = (

            select(

                Producto.id,

                Producto.codigo,

                Producto.nombre,

                Inventario.stock_actual,

                func.coalesce(

                    func.sum(
                        VentaDetalle.cantidad
                    ),

                    0,

                ).label(
                    "vendidos"
                ),

            )

            .join(
                Inventario,
                Inventario.producto_id == Producto.id,
            )

            .outerjoin(
                VentaDetalle,
                VentaDetalle.producto_id == Producto.id,
            )

            .group_by(

                Producto.id,

                Producto.codigo,

                Producto.nombre,

                Inventario.stock_actual,

            )

            .order_by(
                Producto.nombre
            )

        )

        return self.session.execute(stmt).all()


    def valor_productos(self):

        stmt = (

            select(
                Producto.id,
                Producto.codigo,
                Producto.nombre,

                (
                    Inventario.stock_actual
                    * Producto.precio_compra_actual
                ).label("valor")

            )

            .join(
                Inventario,
                Inventario.producto_id == Producto.id
            )

            .order_by(
                (
                    Inventario.stock_actual
                    * Producto.precio_compra_actual
                ).desc()
            )

        )

        return self.session.execute(stmt).all()