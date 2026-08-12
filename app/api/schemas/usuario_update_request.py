from pydantic import BaseModel

from app.modules.usuarios.enums.rol_usuario import RolUsuario


class UsuarioUpdateRequest(BaseModel):

    nombre_completo: str | None = None

    email: str | None = None

    password: str | None = None

    rol: RolUsuario | None = None