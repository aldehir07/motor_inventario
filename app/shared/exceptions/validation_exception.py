from app.shared.exceptions.business_exception import BusinessException


class ValidationException(BusinessException):
    """Error de validación."""