from typing import Annotated

from fastapi import APIRouter, Depends, status

from app.api.dependencies.catalogo import (
    get_catalogo_service,
)

from app.api.schemas.api_response import ApiResponse

from app.api.utils.responses import success_response

from app.modules.catalogo.services.catalogo_service import (
    CatalogoService,
)

from app.modules.catalogo.schemas.catalogo_schema import (
    CatalogoItemResponse,
    ProveedorResponse,
    UnidadMedidaResponse,
    MarcaResponse
)


router = APIRouter(
    prefix="/catalogos",
    tags=["Catálogos"],
)

@router.get(
    "/categorias",
    response_model=ApiResponse[
        list[CatalogoItemResponse]
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar categorías",
)
def listar_categorias(
    service: Annotated[
        CatalogoService,
        Depends(get_catalogo_service),
    ],
):
    categorias = service.listar_categorias()

    return success_response(
        categorias,
        "Categorías obtenidas correctamente.",
    )


@router.get(
    "/marcas",
    response_model=ApiResponse[
        list[CatalogoItemResponse]
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar marcas",
)
def listar_marcas(
    service: Annotated[
        CatalogoService,
        Depends(get_catalogo_service),
    ],
):
    marcas = service.listar_marcas()

    return success_response(
        marcas,
        "Marcas obtenidas correctamente.",
    )


@router.get(
    "/proveedores",
    response_model=ApiResponse[
        list[ProveedorResponse]
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar proveedores",
)
def listar_proveedores(
    service: Annotated[
        CatalogoService,
        Depends(get_catalogo_service),
    ],
):
    proveedores = service.listar_proveedores()

    return success_response(
        proveedores,
        "Proveedores obtenidos correctamente.",
    )


@router.get(
    "/unidades-medida",
    response_model=ApiResponse[
        list[UnidadMedidaResponse]
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar unidades de medida",
)
def listar_unidades_medida(
    service: Annotated[
        CatalogoService,
        Depends(get_catalogo_service),
    ],
):
    unidades = service.listar_unidades_medida()

    return success_response(
        unidades,
        "Unidades de medida obtenidas correctamente.",
    )


@router.get(
    "/marcas",
    response_model=ApiResponse[
        list[MarcaResponse]
    ],
    status_code=status.HTTP_200_OK,
    summary="Listar marcas",
)
def listar_marcas(
    service: Annotated[
        CatalogoService,
        Depends(get_catalogo_service),
    ],
):

    marcas = service.listar_marcas()

    return success_response(
        marcas,
        "Marcas obtenidas correctamente"
    )