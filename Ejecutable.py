from electrodomestico import Electrodomestico
from lavadora import Lavadora
from television import Television

electrodomesticos = [
    Electrodomestico(),
    Electrodomestico(200, 30, "rojo", "A"),
    Lavadora(),
    Lavadora(35, 300, 40, "blanco", "B"),
    Lavadora(50, 500, 60, "blanco", "A"),
    Television(),
    Television(50, True, 600, 20, "negro", "A"),
    Television(42, False, 400, 15, "negro", "C"),
    Electrodomestico(250, 80, "gris", "D"),
    Television(55, True, 700, 25, "negro", "B")
]

total_electrodomesticos = 0
total_lavadoras = 0
total_televisiones = 0

for electrodomestico in electrodomesticos:

    precio = electrodomestico.precio_final()

    total_electrodomesticos += precio

    if isinstance(electrodomestico, Lavadora):
        total_lavadoras += precio

    elif isinstance(electrodomestico, Television):
        total_televisiones += precio

print("Total Electrodomésticos:", total_electrodomesticos)
print("Total Lavadoras:", total_lavadoras)
print("Total Televisiones:", total_televisiones)
