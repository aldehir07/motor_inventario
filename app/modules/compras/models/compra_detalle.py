from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin


if TYPE_CHECKING:
    from app.modules.compras.models.compra import Compra
    from app.modules.catalogo.models.producto import Producto


class CompraDetalle(IdMixin, BaseModel):

    __tablename__ = "compra_detalles"


    compra_id: Mapped[int] = mapped_column(
        ForeignKey("compras.id"),
        nullable=False,
        index=True,
    )


    producto_id: Mapped[int] = mapped_column(
        ForeignKey("productos.id"),
        nullable=False,
        index=True,
    )


    cantidad: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )


    costo_unitario: Mapped[Decimal] = mapped_column(
        Numeric(12,2),
        nullable=False,
    )


    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(12,2),
        nullable=False,
    )


    compra: Mapped["Compra"] = relationship(
        back_populates="detalles"
    )


    producto: Mapped["Producto"] = relationship()