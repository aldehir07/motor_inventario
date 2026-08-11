from sqlalchemy.orm import sessionmaker

from app.database.connection import engine

# Registrar todos los modelos antes de crear sesiones
import app.database.model_registry

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)