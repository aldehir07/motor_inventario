from decimal import Decimal
import math

from sqlalchemy.orm import Session

from app.config.logger import logger

from app.modules.catalogo.models.producto import Producto
from app.modules.catalogo.repositories.catalogo_repository import CatalogoRepository
from app.modules.catalogo.schemas.producto_schema import ProductoCreate
from app.shared.exceptions.duplicate_exception import DuplicateException
from app.shared.exceptions.not_found_exception import NotFoundException

from app.modules.catalogo.models.categoria import Categoria
from app.modules.catalogo.models.proveedor import Proveedor
from app.modules.catalogo.models.marca import Marca
from app.modules.catalogo.models.unidad_medida import UnidadMedida

from app.shared.repositories.base_repository import BaseRepository

from app.modules.catalogo.schemas.producto_filter import ProductoFilter
from app.modules.catalogo.schemas.producto_schema import ProductoUpdate

from app.shared.schemas.paginated_result import PaginatedResult

class CatalogoService:

    def __init__(self, session: Session):
        self.session = session
        self.repository = CatalogoRepository(session)
        self.categoria_repository = BaseRepository(session, Categoria)
        self.proveedor_repository = BaseRepository(session, Proveedor)
        self.marca_repository = BaseRepository(session, Marca)
        self.unidad_repository = BaseRepository(session, UnidadMedida)

    def crear_producto(self, data: ProductoCreate) -> Producto:

        logger.info("Iniciando cracion del producto '{}'", data.codigo)

        if not self.categoria_repository.exists(id=data.categoria_id):
            logger.warning("Categoria {} no encontrada", data.categoria_id)
            raise NotFoundException("La categoría no existe.")

        if not self.proveedor_repository.exists(id=data.proveedor_id):
            logger.warning("Proveedor {} no encontrado", data.proveedor_id)
            raise NotFoundException("El proveedor no existe.")

        if not self.marca_repository.exists(id=data.marca_id):
            logger.warning("Marca {} no encontrado", data.marca_id)
            raise NotFoundException("La marca no existe.")

        if not self.unidad_repository.exists(id=data.unidad_medida_id):
            logger.warning("Unidad de medida {} no encontrado", data.unidad_medida_id)
            raise NotFoundException("La unidad de medida no existe.")

        if self.repository.get_by_codigo(data.codigo):
            raise DuplicateException(f"Ya existe un producto con el código '{data.codigo}'.")

        if self.repository.get_by_sku(data.sku):
            raise DuplicateException(f"Ya existe un producto con el SKU '{data.sku}'.")

        producto = Producto(
            categoria_id =data.categoria_id,
            proveedor_id =data.proveedor_id,
            marca_id =data.marca_id,
            unidad_medida_id =data.unidad_medida_id,
            codigo =data.codigo,
            sku= data.sku,
            nombre= data.nombre,
            descripcion= data.descripcion,
            precio_compra_actual= data.precio_compra_actual,
            precio_venta_actual= data.precio_venta_actual,
            stock_minimo= data.stock_minimo,
            stock_maximo= data.stock_maximo
        )

        self.repository.add(producto)

        logger.info("Guardando porducto '{}' en la base de datos", data.codigo)
        self.session.commit()

        self.session.refresh(producto)
        logger.success("Producto '{}' creado correctamente con ID {}",
            producto.codigo,
            producto.id,
        )
        return producto

    def obtener_producto_port_id(self, producto_id: int) -> Producto:
        producto = self.repository.get_by_id(producto_id)

        if not producto:
            raise NotFoundException(f"No existe el producto con ID {producto_id}")


        return producto

    def obtener_producto_por_codigo(self, codigo: str) -> Producto:
        producto = self.repository.get_by_codigo(codigo)

        if not producto:
            raise NotFoundException(f"No existe el producto con codigo {codigo}")


        return producto

    def buscar_producto(self, texto: str) -> list[Producto]:
        return self.repository.buscar_por_nombre(texto)

    def listar_productos(
        self,
        pagina: int = 1,
        limite: int = 50,
        filtros: ProductoFilter | None = None,
    ):
        productos, total = self.repository.get_paginated(
            pagina,
            limite,
            filtros
        )

        paginas = math.ceil(total / limite)

        return PaginatedResult(
            items=productos,
            total=total,
            pagina=pagina,
            limite=limite,
            paginas=paginas,
        )

    def filtrar_productos(self,filtros: ProductoFilter):
        return self.repository.filtrar(filtros)

    def actualizar_producto(self, producto_id: int, data: ProductoUpdate):

        producto = self.repository.get_by_id(producto_id)

        if not producto:
            raise NotFoundException("El producto no existe.")

        cambios = data.model_dump(exclude_unset=True)

        self.repository.update(producto, cambios)

        logger.info("Actualizando producto ID {}", producto_id)
        self.session.commit()

        self.session.refresh(producto)
        logger.success("Producto {} actualizado correctamente", producto.codigo)

        return producto

    def desactivar_producto(self, producto_id:int):

        producto = self.repository.get_by_id(producto_id)

        if not producto:
            raise NotFoundException("El producto no existe.")

        producto.activo = False

        logger.warning("Desactivando producto {}", producto.codigo)
        self.session.commit()

        self.session.refresh(producto)

        logger.success(
            "Producto {} desactivado correctamente",
            producto.codigo,
        )

        return producto

    def listar_categorias(self):
        return self.categoria_repository.get_all(
            activo=True
        )

    def listar_marcas(self):
        return self.marca_repository.get_all(
            activo=True
        )


    def listar_proveedores(self):
        return self.proveedor_repository.get_all(
            activo=True
        )


    def listar_unidades_medida(self):
        return self.unidad_repository.get_all(
            activo=True
        )