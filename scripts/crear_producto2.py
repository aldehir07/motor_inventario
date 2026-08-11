from decimal import Decimal

from app.database.session import SessionLocal
from app.modules.catalogo.services.catalogo_service import CatalogoService
from app.modules.catalogo.schemas.producto_schema import ProductoCreate

def main():
    session = SessionLocal()

    try:
        service = CatalogoService(session)

        data = ProductoCreate(
            categoria_id=1,
            proveedor_id=1,
            marca_id=1,
            unidad_medida_id=1,
            codigo="P000002",
            sku="DELL-002",
            nombre="Monitor HD 4K",
            descripcion="Monitor de prueba",
            precio_compra_actual=Decimal("650.00"),
            precio_venta_actual=Decimal("850.00"),
            stock_minimo=5,
            stock_maximo=25,
        )

        producto = service.crear_producto(data)

        print("=" * 40)
        print("Producto creado correctamente")
        print("=" * 40)
        print(f"ID: {producto.id}")
        print(f"Código: {producto.codigo}")
        print(f"Nombre: {producto.nombre}")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()


if __name__ == "__main__":
    main()