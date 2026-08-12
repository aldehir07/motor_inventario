from __future__ import annotations

from sqlalchemy import Boolean, Enum, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.modules.base_model import BaseModel
from app.modules.mixins import IdMixin
from app.modules.usuarios.enums.rol_usuario import RolUsuario


class Usuario(IdMixin, BaseModel):
    __tablename__ = "usuarios"

    __table_args__ = (
        UniqueConstraint("email", name="uq_usuarios_email"),
    )

    nombre_completo: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    rol: Mapped[RolUsuario] = mapped_column(
        Enum(RolUsuario),
        default=RolUsuario.USUARIO,
        nullable=False,
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, email='{self.email}')"