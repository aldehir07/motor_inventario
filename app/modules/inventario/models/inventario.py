from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin
from app.modules.inventario.models.movimiento_inventario import MovimientoInventario

if TYPE_CHECKING:
    from app.modules.catalogo.models.producto import Producto
    from app.modules.inventario.models.movimiento_inventario import MovimientoInventario


class Inventario(IdMixin, BaseModel):
    __tablename__ = "inventarios"

    producto_id: Mapped[int] = mapped_column(
        ForeignKey("productos.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    stock_actual: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    stock_reservado: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    producto: Mapped["Producto"] = relationship(
        back_populates="inventario"
    )

    movimientos: Mapped[list["MovimientoInventario"]] = relationship(
        back_populates="inventario",
        cascade="all, delete-orphan",
        order_by="MovimientoInventario.fecha_creacion",
    )