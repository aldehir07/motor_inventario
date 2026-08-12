from pydantic import BaseModel

from app.modules.usuarios.enums.rol_usuario import RolUsuario


class UsuarioCreateRequest(BaseModel):

    nombre_completo: str

    email: str

    password: str

    rol: RolUsuario = RolUsuario.USUARIO