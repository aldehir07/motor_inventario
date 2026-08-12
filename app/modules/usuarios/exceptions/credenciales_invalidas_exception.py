from app.shared.exceptions.business_exception import BusinessException


class CredencialesInvalidasException(BusinessException):
    """El email o la contraseña proporcionados son incorrectos."""