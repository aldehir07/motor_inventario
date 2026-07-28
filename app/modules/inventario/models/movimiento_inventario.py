from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin
from app.modules.inventario.enums.tipo_movimiento import TipoMovimiento

if TYPE_CHECKING:
    from app.modules.inventario.models.inventario import Inventario


class MovimientoInventario(IdMixin, BaseModel):
    __tablename__ = "movimientos_inventario"

    inventario_id: Mapped[int] = mapped_column(
        ForeignKey("inventarios.id"),
        nullable=False,
        index=True,
    )

    tipo: Mapped[TipoMovimiento] = mapped_column(
        Enum(TipoMovimiento),
        nullable=False,
    )

    cantidad: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    stock_anterior: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    stock_nuevo: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    motivo: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    referencia: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    inventario: Mapped["Inventario"] = relationship(
        back_populates="movimientos"
    )