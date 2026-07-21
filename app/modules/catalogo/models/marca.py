from sqlalchemy import Boolean, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.catalogo.models.producto import Producto


class Marca(IdMixin, BaseModel):
    __tablename__ = "marcas"

    __table_args__ = (
        UniqueConstraint("nombre", name="uq_marcas_nombre"),
    )

    nombre: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    descripcion: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    productos: Mapped[list["Producto"]] = relationship(
        back_populates="marca"
    )