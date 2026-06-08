electrodomestico.py

class Electrodomestico:
    # constantes
    PRECIO_BASE = 100
    COLORES_VALIDOS = ["blanco", "negro", "rojo", "azul", "gris"]
    CONSUMO_VALIDO = ["A", "B", "C", "D", "E", "F"]
    


    def __init__(self, precio_base=PRECIO_BASE, peso=5, color="blanco", consumo="F"):
        self.precio_base = precio_base
        self.peso = int(peso)
        self.color = self.comprobar_color(color)
        self.consumo = self.comprobar_consumo(consumo)
        

    def comprobar_consumo(self, consumo):
        if consumo in self.CONSUMO_VALIDO:
            return consumo
        return "F"

    def comprobar_color(self, color):
        if color in self.COLORES_VALIDOS:
            return color
        return "blanco"

    def precio_final(self):
        precio = self.precio_base

        # aumento por consumo
        if self.consumo == "A":
            precio += 100
        elif self.consumo == "B":
            precio += 80
        elif self.consumo == "C":
            precio += 60
        elif self.consumo == "D":
            precio += 50
        elif self.consumo == "E":
            precio += 30
        else:
            precio += 10

        # aumento por peso
        if self.peso < 20:
            precio += 10
        elif self.peso < 50:
            precio += 50
        elif self.peso < 80:
            precio += 80
        else:
            precio += 100

        return precio
