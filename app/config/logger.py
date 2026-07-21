from pathlib import Path
import sys

from loguru import logger

from app.config.settings import settings

# Crear la carpeta de logs si no existe
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# Eliminar la configuración por defecto
logger.remove()

# Mostrar logs en la consola
logger.add(
    sys.stderr,
    level=settings.LOG_LEVEL,
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level: <8}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
           "<level>{message}</level>"
)

# Guardar logs en archivo
logger.add(
    "logs/app.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level=settings.LOG_LEVEL,
    encoding="utf-8",
    enqueue=True
)