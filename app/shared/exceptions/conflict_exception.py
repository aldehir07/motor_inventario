from app.shared.exceptions.business_exception import (
    BusinessException,
)


class ConflictException(BusinessException):
    """Conflicto con el estado actual del recurso."""