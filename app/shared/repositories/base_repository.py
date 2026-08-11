from typing import Any, Generic, TypeVar

from sqlalchemy import func, select
from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):

    def __init__(self, session: Session, model: type[T]):
        self.session = session
        self.model = model

    def add(self, entity: T) -> T:
        self.session.add(entity)
        return entity

    def get_by_id(self, entity_id: int) -> T | None:
        return self.session.get(self.model, entity_id)

    def get_one(self, **filters: Any) -> T | None:
        stmt = select(self.model).filter_by(**filters)
        return self.session.scalar(stmt)

    def get_all(self, limit: int = 100, offset: int = 0) -> list[T]:
        stmt = select(self.model)
        return list(self.session.scalars(stmt))

    def exists(self, **filters: Any) -> bool:
        stmt = select(self.model).filter_by(**filters)
        return self.session.scalar(stmt) is not None

    def delete(self, entity: T) -> None:
        self.session.delete(entity)

    def count(self) -> int:
        stmt = select(func.count()).select_from(self.model)
        return self.session.scalar(stmt) or 0