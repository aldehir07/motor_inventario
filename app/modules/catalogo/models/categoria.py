from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.modules.catalogo.models.producto import Producto

class Categoria(IdMixin, BaseModel):
    __tablename__= "categorias"

    nombre:Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
        nullable=False
    )

    descripcion: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    productos: Mapped[list["Producto"]] = relationship(
    back_populates="categoria"
)

    def __repr__(self) -> str:
        return f"Categoria(id={self.id}, nombre='{self.nombre}')"