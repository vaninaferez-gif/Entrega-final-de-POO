from electrodomestico import Electrodomestico


class Lavadora(Electrodomestico):

    CARGA_DEFECTO = 5

    def _init_(self,
                 carga=CARGA_DEFECTO,
                 precio_base=Electrodomestico.PRECIO_BASE_DEFECTO,
                 peso=Electrodomestico.PESO_DEFECTO,
                 color=Electrodomestico.COLOR_DEFECTO,
                 consumo_energetico=Electrodomestico.CONSUMO_DEFECTO):

        super()._init_(precio_base, peso, color, consumo_energetico)
        self._carga = carga

    def get_carga(self):
        return self._carga

    def precio_final(self):

        precio = super().precio_final()

        if self._carga > 30:
            precio += 50

        return precio
