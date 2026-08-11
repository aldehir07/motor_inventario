from pydantic import BaseModel, ConfigDict

class InventarioResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    producto_id: int
    stock_actual: int
    stock_reservado: int