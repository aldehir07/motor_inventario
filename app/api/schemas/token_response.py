from pydantic import BaseModel

from app.api.schemas.usuario_response import UsuarioResponse


class TokenResponse(BaseModel):

    access_token: str

    token_type: str = "bearer"

    usuario: UsuarioResponse