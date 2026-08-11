from dataclasses import dataclass


@dataclass(frozen=True)
class ConfiguracionML:
    """
    Configuración general del Motor Inteligente.
    """

    dias_cobertura: int = 30

    riesgo_critico_dias: int = 7

    riesgo_alto_dias: int = 15

    riesgo_medio_dias: int = 30

    exceso_factor: float = 1.50

    dias_exceso_inventario: int = 60