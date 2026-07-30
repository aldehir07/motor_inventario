from decimal import Decimal

from sqlalchemy.orm import Session

from app.modules.catalogo.models.producto import Producto
from app.modules.catalogo.repositories.catalogo_repository import CatalogoRepository

from app.modules.ventas.models.venta import Venta
from app.modules.ventas.models.venta_detalle import VentaDetalle

from app.modules.ventas.enums.estado_venta import EstadoVenta

from app.modules.ventas.repositories.venta_repository import VentaRepository
from app.modules.ventas.repositories.venta_detalle_repository import (
    VentaDetalleRepository,
)

from app.modules.ventas.schemas.venta_schema import VentaCreate

from app.shared.exceptions.duplicate_exception import DuplicateException
from app.shared.exceptions.not_found_exception import NotFoundException

from app.shared.repositories.base_repository import BaseRepository

from app.config.logger import logger

class VentaService:

    def __init__(self, session: Session):
        self.session = session

        self.venta_repository = VentaRepository(session)

        self.detalle_repository = VentaDetalleRepository(session)

        self.producto_repository = CatalogoRepository(session)

    def _validar_numero_documento(
        self,
        numero_documento: str,
    ):

        if self.venta_repository.get_by_numero_documento(
            numero_documento
        ):
            raise DuplicateException(
                f"Ya existe la venta '{numero_documento}'."
            )

    def _validar_producto(
        self,
        producto_id: int,
    ) -> Producto:

        producto = self.producto_repository.get_by_id(
            producto_id
        )

        if producto is None:
            raise NotFoundException(
                f"Producto {producto_id} no existe."
            )

        return producto

    def _calcular_subtotal(
        self,
        cantidad: int,
        precio: Decimal,
    ) -> Decimal:

        return Decimal(cantidad) * precio

    def _crear_detalle(
        self,
        venta: Venta,
        producto: Producto,
        cantidad: int,
    ) -> VentaDetalle:

        subtotal = self._calcular_subtotal(
            cantidad,
            producto.precio_venta_actual,
        )

        return VentaDetalle(
            venta=venta,
            producto_id=producto.id,
            cantidad=cantidad,
            precio_unitario=producto.precio_venta_actual,
            subtotal=subtotal,
        )

    def _calcular_total(
        self,
        subtotal: Decimal,
        impuesto: Decimal,
    ) -> Decimal:

        return subtotal + impuesto

    def crear_venta(
        self,
        data: VentaCreate,
    ) -> Venta:

        self._validar_numero_documento(
            data.numero_documento
        )

        venta = Venta(
            numero_documento=data.numero_documento,
            fecha=data.fecha,
            subtotal=Decimal("0.00"),
            impuesto=data.impuesto,
            total=Decimal("0.00"),
            estado=EstadoVenta.BORRADOR,
        )

        self.venta_repository.add(venta)

        subtotal = Decimal("0.00")

        for item in data.detalles:

            producto = self._validar_producto(
                item.producto_id
            )

            detalle = self._crear_detalle(
                venta=venta,
                producto=producto,
                cantidad=item.cantidad,
            )

            subtotal += detalle.subtotal

            self.detalle_repository.add(
                detalle
            )

        venta.subtotal = subtotal

        venta.total = self._calcular_total(
            subtotal,
            data.impuesto,
        )

        self.session.commit()

        self.session.refresh(venta)

        logger.success(
            "Venta {} creada correctamente.",
            venta.numero_documento,
        )

        return venta