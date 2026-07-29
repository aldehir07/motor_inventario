from decimal import Decimal

from sqlalchemy.orm import Session

from app.config.logger import logger

from app.modules.catalogo.models.producto import Producto
from app.modules.catalogo.models.proveedor import Proveedor

from app.modules.compras.enums.estado_compra import EstadoCompra
from app.modules.compras.models.compra import Compra
from app.modules.compras.models.compra_detalle import CompraDetalle

from app.modules.compras.repositories.compra_repository import (
    CompraRepository,
)
from app.modules.compras.repositories.compra_detalle_repository import (
    CompraDetalleRepository,
)

from app.modules.compras.exceptions.estado_compra_exception import (
    EstadoCompraException,
)
from app.modules.inventario.services.inventario_service import (
    InventarioService,
)

from app.modules.inventario.schemas.movimiento_schema import (
    RegistrarEntrada,
)
from app.modules.compras.schemas.compra_schema import CompraCreate

from app.shared.exceptions.duplicate_exception import DuplicateException
from app.shared.exceptions.not_found_exception import NotFoundException
from app.shared.repositories.base_repository import BaseRepository

class CompraService:
    def __init__(self, session: Session):
        self.session= session

        self.compra_respository = CompraRepository(session)
        self.detalle_repository = CompraDetalleRepository(session)

        self.proveedor_repository = BaseRepository(session, Proveedor)

        self.producto_repository = BaseRepository(session, Producto)

        self.inventario_sevice = InventarioService(session)

    def _validar_proveedor(self, proveedor_id: int):
        if not self.proveedor_repository.exists(
            id=proveedor_id
        ):
            raise NotFoundException("El proveedor no existe.")

    def _validar_producto(self, producto_id: int):
        if not self.producto_repository.exists(
            id=producto_id
        ):
            raise NotFoundException(f"Producto {producto_id} no existe.")

    def _validar_documento(self, numero_documento: str):
        if self.compra_respository.get_by_numero_documento(
            numero_documento
        ):
            raise DuplicateException("El numero de documento ya existe.")

    def _validar_estado_borrador(
        self,
        compra: Compra,
    ):

        if compra.estado != EstadoCompra.BORRADOR:

            raise EstadoCompraException(
                "Solo las compras en estado BORRADOR pueden confirmarse."
            )

    def _calcular_subtotal(
        self,
        cantidad: int,
        costo_unitario: Decimal,
    ) -> Decimal:

        return Decimal(cantidad) * costo_unitario

    def _validar_subtotal(self, cantidad: int, costo_unitario: Decimal) -> Decimal:
        return Decimal

    def _calcular_totales(
            self, 
            detalles: list[CompraDetalle], 
            impuesto: Decimal
    ) -> tuple[Decimal, Decimal]:
        subtotal = sum(
            detalle.subtotal for detalle in detalles
        )

        total = subtotal + impuesto

        return subtotal, total

    def crear_compra(self, data: CompraCreate):
        self._validar_proveedor(data.proveedor_id)
        self._validar_documento(data.numero_documento)

        try:
            logger.info("Creando compra {}", data.numero_documento)

            compra = Compra(
                proveedor_id=data.proveedor_id,
                numero_documento=data.numero_documento,
                fecha=data.fecha,
                impuesto=data.impuesto,
                subtotal=Decimal("0"),
                total=Decimal("0"),
                estado=EstadoCompra.BORRADOR
            )

            self.compra_respository.add(compra)

            self.session.flush()

            detalles = []

            for item in data.detalles:
                self._validar_producto(item.producto_id)

                subtotal = self._calcular_subtotal(
                    item.cantidad,
                    item.costo_unitario
                )

                detalle = CompraDetalle(
                    compra_id=compra.id,
                    producto_id=item.producto_id,
                    cantidad=item.cantidad,
                    costo_unitario=item.costo_unitario,
                    subtotal=subtotal
                )

                self.detalle_repository.add(detalle)

                detalles.append(detalle)

            subtotal, total = self._calcular_totales(
                detalles,
                data.impuesto
            )
            compra.subtotal = subtotal
            compra.total = total

            self.session.commit()
            self.session.refresh(compra)

            logger.success("Compra {} creando correctamente.", compra.numero_documento)

            return compra
        
        except Exception as e:
            self.session.rollback()
            logger.exception("Error creando compra: {}", e)
            raise

    def confirmar_compra(self, compra_id: int,):
        compra = self.compra_respository.get_by_id_with_detalles(
            compra_id
        )

        if compra is None:
            raise NotFoundException(
                "La compra no existe."
            )

        self._validar_estado_borrador(compra)

        try:

            logger.info(
                "Confirmando compra {}",
                compra.numero_documento,
            )

            for detalle in compra.detalles:

                self.inventario_sevice.registrar_entrada(
                    RegistrarEntrada(
                        producto_id=detalle.producto_id,
                        cantidad=detalle.cantidad,
                        motivo=f"Compra {compra.numero_documento}",
                        referencia=str(compra.id)
                    ),
                    auto_commit=False
                )

            compra.estado = EstadoCompra.CONFIRMADA

            self.session.commit()

            self.session.refresh(compra)

            logger.success("Compra {} confirmada correctamente.",compra.numero_documento)

            return compra

        except Exception as e:
            self.session.rollback()
            logger.exception("Error confirmando compra: {}", e)
            raise