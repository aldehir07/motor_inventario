from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin

if TYPE_CHECKING:
    from app.modules.catalogo.models.categoria import Categoria
    from app.modules.catalogo.models.proveedor import Proveedor
    from app.modules.catalogo.models.marca import Marca
    from app.modules.catalogo.models.unidad_medida import UnidadMedida


class Producto(IdMixin, BaseModel):
    __tablename__ = "productos"

    __table_args__ = (
        UniqueConstraint("codigo", name="uq_productos_codigo"),
        UniqueConstraint("sku", name="uq_productos_sku"),
        UniqueConstraint("codigo_barras", name="uq_productos_codigo_barras"),
    )

    categoria_id: Mapped[int] = mapped_column(
        ForeignKey("categorias.id"),
        nullable=False,
        index=True,
    )

    proveedor_id: Mapped[int] = mapped_column(
        ForeignKey("proveedores.id"),
        nullable=False,
        index=True,
    )

    marca_id: Mapped[int] = mapped_column(
        ForeignKey("marcas.id"),
        nullable=False,
        index=True,
    )

    unidad_medida_id: Mapped[int] = mapped_column(
        ForeignKey("unidades_medida.id"),
        nullable=False,
        index=True,
    )

    codigo: Mapped[str] = mapped_column(String(30), nullable=False, index=True)

    sku: Mapped[str] = mapped_column(String(50), nullable=False, index=True)

    codigo_barras: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
        index=True,
    )

    nombre: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    descripcion: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    precio_compra_actual: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    precio_venta_actual: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    stock_minimo: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    stock_maximo: Mapped[int] = mapped_column(
        Integer,
        default=100,
        nullable=False,
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    categoria: Mapped["Categoria"] = relationship(back_populates="productos")
    proveedor: Mapped["Proveedor"] = relationship(back_populates="productos")
    marca: Mapped["Marca"] = relationship(back_populates="productos")
    unidad_medida: Mapped["UnidadMedida"] = relationship(back_populates="productos")