from app.shared.exceptions.business_exception import BusinessException


class DuplicateException(BusinessException):
    """Registro duplicado."""
    pass