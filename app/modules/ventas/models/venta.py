from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Date, Enum, ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin

from app.modules.ventas.enums.estado_venta import EstadoVenta

if TYPE_CHECKING:
    from app.modules.ventas.models.venta_detalle import VentaDetalle


class Venta(IdMixin, BaseModel):
    __tablename__ = "ventas"

    numero_documento: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    fecha: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    subtotal: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    impuesto: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    total: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    estado: Mapped[EstadoVenta] = mapped_column(
        Enum(EstadoVenta),
        default=EstadoVenta.BORRADOR,
        nullable=False,
    )

    detalles: Mapped[list["VentaDetalle"]] = relationship(
        back_populates="venta",
        cascade="all, delete-orphan",
    )