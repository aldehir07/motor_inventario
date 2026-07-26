from app.database.session import SessionLocal

from app.modules.catalogo.services.catalogo_service import CatalogoService

from app.modules.catalogo.schemas.producto_schema import ProductoUpdate


session = SessionLocal()

service = CatalogoService(session)


producto = service.actualizar_producto(
    1,
    ProductoUpdate(
        precio_venta_actual=900
    )
)


print(producto.nombre)
print(producto.precio_venta_actual)


session.close()