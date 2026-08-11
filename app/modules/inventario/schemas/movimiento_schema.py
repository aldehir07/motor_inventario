from pydantic import BaseModel, Field


class RegistrarEntrada(BaseModel):
    producto_id: int
    cantidad: int = Field(gt=0)
    motivo: str
    referencia: str | None = None

class RegistrarSalida(BaseModel):
    producto_id: int
    cantidad: int = Field(gt=0)
    motivo: str
    referencia: str | None = None

class AjustarStock(BaseModel):
    producto_id: int
    nuevo_stock: int = Field(gt=0)
    motivo: str
    referencia: str | None = None