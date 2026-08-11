from sqlalchemy import select, func
from sqlalchemy.orm import Session

from app.modules.catalogo.models.producto import Producto
from app.shared.repositories.base_repository import BaseRepository
from app.modules.catalogo.schemas.producto_filter import ProductoFilter

class CatalogoRepository(BaseRepository[Producto]):
    def __init__(self, session: Session):
        super().__init__(session, Producto)

    def get_by_codigo(self, codigo: str) -> Producto | None:
        stmt = select(Producto).where(Producto.codigo == codigo)
        return self.session.scalar(stmt)

    def get_by_sku(self, sku: str) -> Producto | None:
        stmt = select(Producto).where(Producto.sku == sku)
        return self.session.scalar(stmt)

    def buscar_por_nombre(self, texto: str) -> list[Producto]:
        stmt =(
            select(Producto)
            .where(Producto.nombre.ilike(f"%{texto}%"))
            .order_by(Producto.nombre)
        )
        return list(self.session.scalars(stmt))

    def get_paginated(self, pagina: int = 1, limite: int = 50):

        offset = (pagina - 1) * limite

        stmt = (select(Producto).order_by(Producto.nombre).offset(offset).limit(limite))

        items = list(self.session.scalars(stmt))

        total_stmt = select(func.count()).select_from(Producto)

        total = self.session.scalar(total_stmt)

        return items, total

    def filtrar(self,filtros: ProductoFilter):

        stmt = select(Producto)

        if filtros.nombre:
            stmt = stmt.where(Producto.nombre.ilike(f"%{filtros.nombre}%"))

        if filtros.categoria_id:
            stmt = stmt.where(Producto.categoria_id == filtros.categoria_id)

        if filtros.proveedor_id:
            stmt = stmt.where(Producto.proveedor_id == filtros.proveedor_id)

        if filtros.marca_id:
            stmt = stmt.where(Producto.marca_id == filtros.marca_id)

        if filtros.unidad_medida_id:
            stmt = stmt.where(Producto.unidad_medida_id == filtros.unidad_medida_id)

        if filtros.activo is not None:
            stmt = stmt.where(Producto.activo == filtros.activo)

        if filtros.precio_min:
            stmt = stmt.where(Producto.precio_venta_actual >= filtros.precio_min)

        if filtros.precio_max:
            stmt = stmt.where(Producto.precio_venta_actual <= filtros.precio_max)

        stmt = stmt.order_by(Producto.nombre)

        return list(self.session.scalars(stmt))

    def update(self, producto: Producto, data: dict):
        for key, value in data.items():
            setattr(producto, key, value)
        return producto