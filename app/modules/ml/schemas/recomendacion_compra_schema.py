from pydantic import BaseModel


class RecomendacionCompra(BaseModel):

    producto_id: int

    codigo: str

    nombre: str

    stock_actual: int

    stock_minimo: int

    stock_maximo: int

    demanda_estimada: float

    cantidad_recomendada: int

    indice_prioridad: int

    prioridad: str

    motivo: str

    clasificacion_abc: str | None = None

    rotacion: float | None = None