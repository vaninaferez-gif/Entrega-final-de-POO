Ejecutable.py 

from electrodomestico import Electrodomestico
from Lavadora import lavadora
from Television import television

electrodomesticos = [
    Electrodomestico(),
    Electrodomestico(200, 30, "rojo", "A"),
    lavadora(),
    lavadora(35, 300, 40, "blanco", "B"),
    lavadora(50, 500, 60, "blanco", "A"),
    television(),
    television(50, True, 600, 20, "negro", "A"),
    television(42, False, 400, 15, "negro", "C"),
    Electrodomestico(250, 80,  "gris", "D"),
    television(55, True, 700, 25, "negro", "B")
]

total_electrodomesticos = 0
total_lavadoras = 0
total_televisiones = 0

for electrodomestico in electrodomesticos:

    precio = electrodomestico.precio_final()

    total_electrodomesticos += precio

    if isinstance(electrodomestico, lavadora):
        total_lavadoras += precio

    elif isinstance(electrodomestico, television):
        total_televisiones += precio

print("Total Electrodomésticos:", total_electrodomesticos)
print("Total Lavadoras:", total_lavadoras)
print("Total Televisiones:", total_televisiones)
