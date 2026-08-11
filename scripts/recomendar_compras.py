from app.database.session import SessionLocal
from app.modules.ml.services.ml_service import MLService


def main():

    session = SessionLocal()

    try:

        service = MLService(session)

        recomendaciones = service.recomendar_comprar()

        print("=" * 80)
        print("RECOMENDACIONES DE COMPRA")
        print("=" * 80)

        for item in recomendaciones:

            print()
            print("=" * 80)

            print(f"Producto............... {item.codigo} - {item.nombre}")

            print()

            print(f"Stock actual........... {item.stock_actual}")
            print(f"Stock mínimo........... {item.stock_minimo}")
            print(f"Stock máximo........... {item.stock_maximo}")

            print()

            print(f"Demanda estimada....... {item.demanda_estimada:.2f}")
            print(f"Días de stock.......... {item.dias_stock:.2f}")

            print()

            print(f"Cobertura objetivo..... {item.cobertura_dias} días")
            print(f"Stock objetivo......... {item.stock_objetivo}")

            print()

            print(f"Riesgo de quiebre...... {item.riesgo_quiebre}")
            print(f"Rotación............... {item.rotacion}")

            print()

            print(
                f"Exceso inventario...... {'SI' if item.exceso_inventario else 'NO'}"
            )
            print(f"Motivo exceso.......... {item.motivo_exceso}")

            print()

            print(f"Cantidad sugerida...... {item.cantidad_recomendada}")

            print()

            print(f"Prioridad.............. {item.prioridad}")
            print(f"Índice................. {item.indice_prioridad}")

            print()

            if item.clasificacion_abc:
                print(f"Clasificación ABC...... {item.clasificacion_abc}")

            print(f"Motivo final........... {item.motivo}")

            print("=" * 80)

    finally:

        session.close()


if __name__ == "__main__":
    main()