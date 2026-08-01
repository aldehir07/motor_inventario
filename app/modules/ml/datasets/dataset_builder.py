import pandas as pd

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.ventas.models.venta import Venta
from app.modules.ventas.models.venta_detalle import VentaDetalle
from app.modules.catalogo.models.producto import Producto
from app.modules.ventas.enums.estado_venta import EstadoVenta
from app.modules.inventario.models.inventario import Inventario

class DatasetBuilder:

    def __init__(
        self,
        session: Session,
    ):

        self.session = session

    def construir_dataset_ventas(
        self,
    ) -> pd.DataFrame:
        stmt = (

            select(
                Producto.id,
                Producto.codigo,
                Producto.nombre,
                Venta.fecha,
                VentaDetalle.cantidad,
            )
            .join(
                VentaDetalle,
                VentaDetalle.producto_id == Producto.id,
            )
            .join(
                Venta,
                Venta.id == VentaDetalle.venta_id,
            )
            .where(
                Venta.estado == EstadoVenta.CONFIRMADA
            )
            .order_by(
                Venta.fecha
            )
        )

        filas = self.session.execute(stmt).all()

        datos = []

        for fila in filas:

            datos.append(

                {

                    "producto_id": fila.id,

                    "codigo": fila.codigo,

                    "nombre": fila.nombre,

                    "fecha": fila.fecha,

                    "cantidad": fila.cantidad,

                }

            )

        return pd.DataFrame(datos)

    def construir_dataset_inventario(
        self,
    ) -> pd.DataFrame:
        stmt = (

            select(
                Producto.id,
                Producto.codigo,
                Producto.nombre,
                Inventario.stock_actual,
                Producto.stock_minimo,
                Producto.stock_maximo
            )
            .join(
                Inventario,
                Inventario.producto_id == Producto.id,
            )

        )

        filas = self.session.execute(stmt).all()

        datos = []

        for fila in filas:
            datos.append(
                {
                    "producto_id": fila.id,
                    "codigo": fila.codigo,
                    "nombre": fila.nombre,
                    "stock_actual": fila.stock_actual,
                    "stock_minimo": fila.stock_minimo,
                    "stock_maximo": fila.stock_maximo
                }
            )

        return pd.DataFrame(datos)