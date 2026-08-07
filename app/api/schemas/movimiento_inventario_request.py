from pydantic import BaseModel, Field

class EntradaInventarioRequest(BaseModel):
    producto_id: int
    cantidad: int = Field(gt=0)
    motivo: str
    referencia: str | None = None

class SalidaInventarioRequest(BaseModel):
    producto_id: int
    cantidad: int
    motivo: str
    referencia: str | None = None

class AjusteStockRequest(BaseModel):
    producto_id: int
    nuevo_stock: int = Field(gt=0)
    motivo: str
    referencia: str | None = None