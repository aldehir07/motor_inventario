from pydantic import BaseModel


class RecomendacionCompra(BaseModel):

    producto_id: int

    codigo: str

    nombre: str

    stock_actual: int

    stock_minimo: int

    stock_maximo: int

    demanda_estimada: float

    dias_stock: float

    riesgo_quiebre: str

    exceso_inventario: bool

    motivo_exceso: str

    cantidad_recomendada: int

    indice_prioridad: int

    prioridad: str

    motivo: str

    clasificacion_abc: str | None = None

    rotacion: str