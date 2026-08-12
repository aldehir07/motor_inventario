from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies.usuarios import (
    get_usuario_service,
)
from app.api.schemas.api_response import ApiResponse
from app.api.schemas.usuario_create_request import (
    UsuarioCreateRequest,
)
from app.api.schemas.usuario_response import UsuarioResponse
from app.api.schemas.usuario_update_request import (
    UsuarioUpdateRequest,
)
from app.api.utils.responses import success_response
from app.modules.usuarios.schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioUpdate,
)
from app.modules.usuarios.services.usuario_service import (
    UsuarioService,
)

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"],
)


@router.get(
    "",
    response_model=ApiResponse[list[UsuarioResponse]],
    status_code=status.HTTP_200_OK,
    summary="Listar usuarios",
    description="Lista todos los usuarios del sistema.",
)
def listar_usuarios(
    service: Annotated[
        UsuarioService,
        Depends(get_usuario_service),
    ],
):

    usuarios = service.listar_usuarios()

    return success_response(
        [UsuarioResponse.model_validate(u) for u in usuarios],
        "Usuarios obtenidos correctamente.",
    )


@router.get(
    "/{usuario_id}",
    response_model=ApiResponse[UsuarioResponse],
    status_code=status.HTTP_200_OK,
    summary="Obtener usuario por ID",
    description="Obtiene un usuario utilizando su ID.",
)
def obtener_usuario(
    usuario_id: int,
    service: Annotated[
        UsuarioService,
        Depends(get_usuario_service),
    ],
):

    usuario = service.obtener_usuario(usuario_id)

    return success_response(
        UsuarioResponse.model_validate(usuario),
        "Usuario obtenido correctamente.",
    )


@router.post(
    "",
    response_model=ApiResponse[UsuarioResponse],
    status_code=status.HTTP_201_CREATED,
    summary="Crear usuario",
    description="Crea un nuevo usuario del sistema.",
)
def crear_usuario(
    request: UsuarioCreateRequest,
    service: Annotated[
        UsuarioService,
        Depends(get_usuario_service),
    ],
):

    data = UsuarioCreate(**request.model_dump())

    usuario = service.crear_usuario(data)

    return success_response(
        UsuarioResponse.model_validate(usuario),
        "Usuario creado correctamente.",
    )


@router.put(
    "/{usuario_id}",
    response_model=ApiResponse[UsuarioResponse],
    status_code=status.HTTP_200_OK,
    summary="Actualizar usuario",
    description="Actualiza la información de un usuario.",
)
def actualizar_usuario(
    usuario_id: int,
    request: UsuarioUpdateRequest,
    service: Annotated[
        UsuarioService,
        Depends(get_usuario_service),
    ],
):

    data = UsuarioUpdate(**request.model_dump(exclude_unset=True))

    usuario = service.actualizar_usuario(usuario_id, data)

    return success_response(
        UsuarioResponse.model_validate(usuario),
        "Usuario actualizado correctamente.",
    )


@router.patch(
    "/{usuario_id}/desactivar",
    response_model=ApiResponse[UsuarioResponse],
    status_code=status.HTTP_200_OK,
    summary="Desactivar usuario",
    description="Desactiva lógicamente un usuario.",
)
def desactivar_usuario(
    usuario_id: int,
    service: Annotated[
        UsuarioService,
        Depends(get_usuario_service),
    ],
):

    usuario = service.desactivar_usuario(usuario_id)

    return success_response(
        UsuarioResponse.model_validate(usuario),
        "Usuario desactivado correctamente.",
    )