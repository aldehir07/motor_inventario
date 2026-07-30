"""
Registro centralizado de todos los modelos SQLAlchemy.

Este archivo se importa una sola vez al iniciar la aplicación para
garantizar que SQLAlchemy conozca todos los mappers y relaciones.
"""

# ==========================
# Catálogo
# ==========================
from app.modules.catalogo.models.categoria import Categoria
from app.modules.catalogo.models.marca import Marca
from app.modules.catalogo.models.proveedor import Proveedor
from app.modules.catalogo.models.unidad_medida import UnidadMedida
from app.modules.catalogo.models.producto import Producto

# ==========================
# Inventario
# ==========================
from app.modules.inventario.models.inventario import Inventario
from app.modules.inventario.models.movimiento_inventario import MovimientoInventario

# ==========================
# Compras
# ==========================
from app.modules.compras.models.compra import Compra
from app.modules.compras.models.compra_detalle import CompraDetalle

# ==========================
# Ventas
# ==========================
from app.modules.ventas.models.venta import Venta
from app.modules.ventas.models.venta_detalle import VentaDetalle