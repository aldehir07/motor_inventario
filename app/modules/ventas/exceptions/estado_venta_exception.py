from app.shared.exceptions.conflict_exception import (
    ConflictException,
)


class EstadoVentaException(ConflictException):
    """Operación no permitida según el estado de la venta."""