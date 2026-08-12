from app.shared.exceptions.business_exception import BusinessException


class UsuarioInactivoException(BusinessException):
    """El usuario está desactivado y no puede operar en el sistema."""