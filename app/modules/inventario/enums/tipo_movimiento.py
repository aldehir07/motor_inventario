from enum import Enum

class TipoMovimiento(str, Enum):
    ENTRADA = "ENTRADA"
    SALIDA = "SALIDA"
    AJUSTE = "AJUSTE"
    TRANSFERENCIA = "TRANSFERENCIA"
    DEVOLUCION = "DEVOLUCION"