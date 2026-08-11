from enum import Enum


class EstadoVenta(str, Enum):
    BORRADOR = "BORRADOR"
    CONFIRMADA = "CONFIRMADA"
    ANULADA = "ANULADA"