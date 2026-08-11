from typing import Generic
from typing import TypeVar

from pydantic import BaseModel
from pydantic import ConfigDict


T = TypeVar("T")


class PaginatedResult(
    BaseModel,
    Generic[T],
):

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    items: list[T]

    total: int

    pagina: int

    limite: int

    paginas: int