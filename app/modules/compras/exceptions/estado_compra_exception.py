from app.shared.exceptions.conflict_exception import (
    ConflictException,
)


class EstadoCompraException(ConflictException):
    """Operación no permitida según el estado de la compra."""