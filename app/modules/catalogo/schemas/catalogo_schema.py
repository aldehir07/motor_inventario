from pydantic import BaseModel, ConfigDict


class CatalogoItemResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    activo: bool


class UnidadMedidaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    abreviatura: str


class ProveedorResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    activo: bool

class MarcaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str 
    activo: bool