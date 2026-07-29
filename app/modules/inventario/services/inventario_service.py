from sqlalchemy.orm import Session

from app.config.logger import logger

from app.modules.inventario.repositories.inventario_repository import (
    InventarioRepository,
)

from app.modules.inventario.repositories.movimiento_repository import (
    MovimientoRepository,
)
from app.modules.inventario.models.movimiento_inventario import (
    MovimientoInventario,
)
from app.modules.inventario.enums.tipo_movimiento import TipoMovimiento
from app.modules.inventario.schemas.movimiento_schema import (RegistrarEntrada, RegistrarSalida, AjustarStock)
from app.modules.inventario.models.inventario import Inventario
from app.modules.catalogo.models.producto import Producto
from app.shared.repositories.base_repository import BaseRepository

from app.modules.inventario.exceptions.producto_no_encontrado_exception import ProductoNoEncontradoException
from app.modules.inventario.exceptions.cantidad_invalida_exception import CantidadInvalidaException
from app.modules.inventario.exceptions.stock_insuficiente_exception import StockInsuficienteException

class InventarioService:

    def __init__(self, session: Session):

        self.session = session

        self.inventario_repository = InventarioRepository(session)

        self.movimiento_repository = MovimientoRepository(session)

        self.producto_repository = BaseRepository(session, Producto)

    def _validar_producto(self, producto_id: int):
        producto = self.producto_repository.get_by_id(producto_id)

        if producto is None:
            raise ProductoNoEncontradoException(producto_id)
        
        return producto

    def _validar_cantidad(self, cantidad: int):
        if cantidad <= 0:
            raise CantidadInvalidaException(cantidad)

    def _validar_stock(self, stock_actual: int, cantidad: int):
        if stock_actual < cantidad:
            raise StockInsuficienteException(disponible=stock_actual, solicitado=cantidad)

    def _crear_movimiento(
        self,
        inventario: Inventario,
        tipo: TipoMovimiento,
        cantidad: int,
        stock_anterior: int,
        stock_nuevo: int,
        motivo: str,
        referencia: str | None,
    ):

        movimiento = MovimientoInventario(
            inventario_id=inventario.id,
            tipo=tipo,
            cantidad=cantidad,
            stock_anterior=stock_anterior,
            stock_nuevo=stock_nuevo,
            motivo=motivo,
            referencia=referencia,
        )

        self.movimiento_repository.add(
            movimiento
        )

        return movimiento

    def registrar_entrada(self, data: RegistrarEntrada, auto_commit: bool=True):

        self._validar_producto(data.producto_id)
        self._validar_cantidad(data.cantidad)

        try:
            logger.info(
                "Registrando entrada. Producto={}, Cantidad={}",
                data.producto_id,
                data.cantidad,
            )
            inventario = self.inventario_repository.get_by_producto_id(
                data.producto_id
            )
            
            if inventario is None:
                inventario = Inventario(
                    producto_id=data.producto_id, 
                    stock_actual=0,
                    stock_reservado=0
                )
            
                self.inventario_repository.add(inventario)
                self.session.flush()
            
            stock_anterior = inventario.stock_actual
            
            inventario.stock_actual += data.cantidad
            
            stock_nuevo = inventario.stock_actual
            

            self._crear_movimiento(
                inventario=inventario,
                tipo=TipoMovimiento.ENTRADA,
                cantidad=data.cantidad,
                stock_anterior=stock_anterior,
                stock_nuevo=stock_nuevo,
                motivo=data.motivo,
                referencia=data.referencia,
            )
            
            if auto_commit:
                self.session.commit()
                self.session.refresh(inventario)

            logger.success(
                "Entrada registrada. Inventario={}, Stock={}",
                inventario.id,
                inventario.stock_actual,
            )
            return inventario

        except Exception as e:
            if auto_commit:
                self.session.rollback()
            logger.exception("Error registrando entrada: {}",e)
            raise

    def registrar_salida(self, data: RegistrarSalida,):

        self._validar_producto(data.producto_id)
        self._validar_cantidad(data.cantidad)

        try:

            logger.info(
                "Registrando salida. Producto={}, Cantidad={}",
                data.producto_id,
                data.cantidad,
            )

            inventario = self.inventario_repository.get_by_producto_id(
                data.producto_id
            )

            if inventario is None:
                raise ProductoNoEncontradoException(
                    data.producto_id
                )

            self._validar_stock(
                inventario.stock_actual,
                data.cantidad,
            )

            stock_anterior = inventario.stock_actual

            inventario.stock_actual -= data.cantidad

            stock_nuevo = inventario.stock_actual

            self._crear_movimiento(
                inventario=inventario,
                tipo=TipoMovimiento.SALIDA,
                cantidad=data.cantidad,
                stock_anterior=stock_anterior,
                stock_nuevo=stock_nuevo,
                motivo=data.motivo,
                referencia=data.referencia,
            )

            self.session.commit()

            self.session.refresh(inventario)

            logger.success(
                "Salida registrada correctamente. Producto={}, Stock={}",
                data.producto_id,
                inventario.stock_actual,
            )

            return inventario

        except Exception as e:
            self.session.rollback()
            logger.exception("Error registrando salida: {}",e,)
            raise

    def ajustar_stock(self, data: AjustarStock):
        self._validar_producto(data.producto_id)

        try:
            logger.info(
                "Ajustando stock. Producto={}, Nuevo Stock={}",
                data.producto_id,
                data.nuevo_stock,
            )

            inventario = self.inventario_repository.get_by_producto_id(
                data.producto_id
            )

            if inventario is None:

                inventario = Inventario(
                    producto_id=data.producto_id,
                    stock_actual=0,
                    stock_reservado=0,
                )

                self.inventario_repository.add(inventario)

                self.session.flush()

            stock_anterior = inventario.stock_actual

            inventario.stock_actual = data.nuevo_stock

            stock_nuevo = inventario.stock_actual

            self._crear_movimiento(
                inventario=inventario,
                tipo=TipoMovimiento.AJUSTE,
                cantidad=abs(stock_nuevo - stock_anterior),
                stock_anterior=stock_anterior,
                stock_nuevo=stock_nuevo,
                motivo=data.motivo,
                referencia=data.referencia,
            )

            self.session.commit()

            self.session.refresh(inventario)

            logger.success(
                "Stock ajustado correctamente. Producto={}, Stock={}",
                data.producto_id,
                inventario.stock_actual,
            )

            return inventario

        except Exception as e:
            self.session.rollback()
            logger.exception("Error ajustando stock: {}", e,)
            raise