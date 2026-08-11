class BusinessException(Exception):
    """Excepción base para errores de negocio."""
    pass


    def __init__(self, message: str):
        self.message = message
        super().__init__(message)