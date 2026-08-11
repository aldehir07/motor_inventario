class DetectorRotacion:

    def __init__(self):
        pass

    def clasificar(
        self,
        demanda_diaria: float,
    ) -> str:
        """
        Clasifica la rotación de un producto
        según su demanda diaria estimada.
        """

        if demanda_diaria >= 10:
            return "ALTA"

        if demanda_diaria >= 5:
            return "MEDIA"

        if demanda_diaria >= 1:
            return "BAJA"

        return "MUY BAJA"