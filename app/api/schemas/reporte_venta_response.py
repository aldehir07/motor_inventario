from pydantic import BaseModel, ConfigDict


class ProductoMasVendidoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    producto_id: int
    codigo: str
    nombre: str
    cantidad_vendida: int