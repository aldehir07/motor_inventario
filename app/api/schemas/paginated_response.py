from typing import Generic
from typing import TypeVar

from pydantic import BaseModel
from pydantic import ConfigDict


T = TypeVar("T")


class PaginatedResponse(
    BaseModel,
    Generic[T],
):

    model_config = ConfigDict(
        from_attributes=True
    )

    items: list[T]

    total: int

    pagina: int

    limite: int

    paginas: int