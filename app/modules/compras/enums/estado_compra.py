from enum import Enum


class EstadoCompra(str, Enum):
    BORRADOR = "BORRADOR"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"