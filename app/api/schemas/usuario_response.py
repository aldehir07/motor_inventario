from pydantic import BaseModel, ConfigDict

from app.modules.usuarios.enums.rol_usuario import RolUsuario


class UsuarioResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int

    nombre_completo: str

    email: str

    rol: RolUsuario

    activo: bool