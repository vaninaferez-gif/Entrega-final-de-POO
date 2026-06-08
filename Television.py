Television.py

from electrodomestico import Electrodomestico


class television(Electrodomestico):

    RESOLUCION_DEFECTO = 20
    TDT_DEFECTO = False

    def __init__(self,
                 resolucion=RESOLUCION_DEFECTO,
                 tdt=TDT_DEFECTO,
                 precio_base=Electrodomestico.PRECIO_BASE,
                 peso="10",
                 color="negro",
                 consumo_energetico="A"):

        super().__init__(precio_base, peso, color, consumo_energetico)

        self._resolucion = resolucion
        self._tdt = tdt

    def get_resolucion(self):
        return self._resolucion

    def get_tdt(self):
        return self._tdt

    def precio_final(self):

        precio = super().precio_final()

        if self._resolucion > 40:
            precio *= 1.3

        if self._tdt:
            precio += 50

        return precio
