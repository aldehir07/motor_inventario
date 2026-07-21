from sqlalchemy import Boolean, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.catalogo.models.producto import Producto


class UnidadMedida(IdMixin, BaseModel):
    __tablename__ = "unidades_medida"

    __table_args__ = (
        UniqueConstraint("abreviatura", name="uq_unidades_abreviatura"),
    )

    nombre: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        index=True,
    )

    abreviatura: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        index=True,
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    productos: Mapped[list["Producto"]] = relationship(
        back_populates="unidad_medida"
    )