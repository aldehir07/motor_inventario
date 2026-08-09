from datetime import date
from app.database.session import SessionLocal
from app.modules.catalogo.repositories.catalogo_repository import CatalogoRepository
from app.modules.ml.services.ml_service import MLService


def main():
    session = SessionLocal()

    try:
        service = MLService(session)
        catalogo_repo = CatalogoRepository(session)

        # 1. Obtenemos el primer producto disponible para realizar la prueba
        productos = catalogo_repo.get_all(limit=1)
        if not productos:
            print("No hay productos en el catálogo para predecir demanda.")
            return

        producto = productos[0]
        fecha_prediccion = date(2026, 8, 15)

        # 2. Ejecutamos la predicción con la nueva firma
        demanda = service.predecir_demanda(
            producto_id=producto.id,
            fecha=fecha_prediccion,
        )

        print("=" * 60)
        print("PREDICCIÓN DE DEMANDA")
        print("=" * 60)
        print(f"Producto: {producto.codigo} - {producto.nombre}")
        print(f"Fecha predicción: {fecha_prediccion.isoformat()}")
        print(f"Demanda estimada: {demanda:.2f}")
        print("=" * 60)

    finally:
        session.close()


if __name__ == "__main__":
    main()