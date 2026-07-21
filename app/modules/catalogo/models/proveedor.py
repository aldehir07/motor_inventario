from sqlalchemy import Boolean, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin
from app.modules.catalogo.models.producto import Producto

class Proveedor(IdMixin, BaseModel):
    __tablename__ = "proveedores"

    __table_args__ = (
        UniqueConstraint("nombre", name="uq_proveedores_nombre"),
    )

    nombre: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    contacto: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    telefono: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
        index=True,
    )

    direccion: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    productos: Mapped[list["Producto"]] = relationship(
        back_populates="proveedor"
    )

    def __repr__(self) -> str:
        return f"Proveedor(id={self.id}, nombre='{self.nombre}')"