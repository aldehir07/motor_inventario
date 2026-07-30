from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin

if TYPE_CHECKING:
    from app.modules.catalogo.models.producto import Producto
    from app.modules.ventas.models.venta import Venta


class VentaDetalle(IdMixin, BaseModel):
    __tablename__ = "venta_detalles"

    venta_id: Mapped[int] = mapped_column(
        ForeignKey("ventas.id"),
        nullable=False,
        index=True,
    )

    producto_id: Mapped[int] = mapped_column(
        ForeignKey("productos.id"),
        nullable=False,
        index=True,
    )

    cantidad: Mapped[int] = mapped_column(
        nullable=False,
    )

    precio_unitario: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    venta: Mapped["Venta"] = relationship(
        back_populates="detalles",
    )

    producto: Mapped["Producto"] = relationship(back_populates="venta_detalles",)