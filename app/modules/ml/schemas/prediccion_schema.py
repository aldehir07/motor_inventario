from pydantic import BaseModel


class PrediccionDemanda(BaseModel):

    producto_id: int

    demanda_estimada: float

    confianza: float