from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin
from app.modules.compras.enums.estado_compra import EstadoCompra

if TYPE_CHECKING:
    from app.modules.catalogo.models.proveedor import Proveedor
    from app.modules.compras.models.compra_detalle import CompraDetalle


class Compra(IdMixin, BaseModel):
    __tablename__ = "compras"

    proveedor_id: Mapped[int] = mapped_column(
        ForeignKey("proveedores.id"),
        nullable=False,
        index=True,
    )

    numero_documento: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    fecha: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=0,
        nullable=False,
    )

    impuesto: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=0,
        nullable=False,
    )

    total: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        default=0,
        nullable=False,
    )

    estado: Mapped[EstadoCompra] = mapped_column(
        default=EstadoCompra.BORRADOR,
        nullable=False,
    )

    proveedor: Mapped["Proveedor"] = relationship(
        back_populates="compras"
    )

    detalles: Mapped[list["CompraDetalle"]] = relationship(
        back_populates="compra",
        cascade="all, delete-orphan",
    )


from app.modules.compras.models.compra_detalle import CompraDetalle
