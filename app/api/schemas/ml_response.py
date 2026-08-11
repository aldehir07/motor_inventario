from datetime import date
from pydantic import BaseModel, ConfigDict


class PrediccionDemandaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    producto_id: int
    fecha: date
    demanda_estimada: float


class RecomendacionCompraResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

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
    stock_objetivo: int
    cobertura_dias: int