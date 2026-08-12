from app.shared.exceptions.business_exception import BusinessException


class AccesoDenegadoException(BusinessException):
    """El usuario no tiene el rol necesario para esta operación."""