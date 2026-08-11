from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.modules.catalogo.services.catalogo_service import CatalogoService


def get_catalogo_service(

    db: Annotated[
        Session,
        Depends(get_db),
    ],

) -> CatalogoService:

    return CatalogoService(db)