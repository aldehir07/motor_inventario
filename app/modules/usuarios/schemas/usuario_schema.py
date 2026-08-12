from pydantic import BaseModel, ConfigDict, Field

from app.modules.usuarios.enums.rol_usuario import RolUsuario


class UsuarioCreate(BaseModel):

    nombre_completo: str = Field(
        min_length=3,
        max_length=150,
    )

    email: str = Field(
        min_length=5,
        max_length=255,
    )

    password: str = Field(
        min_length=8,
        max_length=128,
    )

    rol: RolUsuario = RolUsuario.USUARIO


class UsuarioUpdate(BaseModel):

    nombre_completo: str | None = Field(
        default=None,
        min_length=3,
        max_length=150,
    )

    email: str | None = Field(
        default=None,
        min_length=5,
        max_length=255,
    )

    password: str | None = Field(
        default=None,
        min_length=8,
        max_length=128,
    )

    rol: RolUsuario | None = None


class UsuarioResponse(BaseModel):

    model_config = ConfigDict(from_attributes=True)

    id: int

    nombre_completo: str

    email: str

    rol: RolUsuario

    activo: bool