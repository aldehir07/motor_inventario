from app.shared.exceptions.business_exception import BusinessException


class NotFoundException(BusinessException):
    """Recurso no encontrado."""