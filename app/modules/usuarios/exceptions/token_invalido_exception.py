from app.shared.exceptions.business_exception import BusinessException


class TokenInvalidoException(BusinessException):
    """El token de acceso no es válido o ha expirado."""