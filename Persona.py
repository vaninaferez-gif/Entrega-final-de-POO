import random


class Persona:

    BAJO_PESO = -1
    PESO_IDEAL = 0
    SOBREPESO = 1

    # Constructor
    def __init__(self, nombre="", edad=0, sexo="H", peso=0.0, altura=0.0):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

        self.__comprobarSexo()
        self.__dni = self.__generaDNI()

    # Constructor con nombre, edad y sexo
    @classmethod
    def constructor2(cls, nombre, edad, sexo):
        return cls(nombre, edad, sexo)

    # Constructor vacío
    @classmethod
    def constructorVacio(cls):
        return cls()

    # IMC
    def calcularIMC(self):
        if self.__altura == 0:
            return None

        imc = self.__peso / (self.__altura ** 2)

        if imc < 20:
            return Persona.BAJO_PESO
        elif imc <= 25:
            return Persona.PESO_IDEAL
        else:
            return Persona.SOBREPESO

    # Mayor de edad
    def esMayorDeEdad(self):
        return self.__edad >= 18

    # Validar sexo
    def __comprobarSexo(self):
        if self.__sexo not in ("H", "M"):
            self.__sexo = "H"

    # DNI
    def __generaDNI(self):
        numero = random.randint(10000000, 99999999)
        letras = "ABCDEF"
        letra = letras[numero % 6]
        return str(numero) + letra

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_sexo(self, sexo):
        self.__sexo = sexo
        self.__comprobarSexo()

    def set_peso(self, peso):
        self.__peso = peso

    def set_altura(self, altura):
        self.__altura = altura

    # Mostrar datos
    def __str__(self):
        return (
            f"Nombre: {self.__nombre}\n"
            f"Edad: {self.__edad}\n"
            f"DNI: {self.__dni}\n"
            f"Sexo: {self.__sexo}\n"
            f"Peso: {self.__peso} kg\n"
            f"Altura: {self.__altura} m"
        )


# Entrada de datos
nombre = input("Ingrese nombre: ")
edad = int(input("Ingrese edad: "))
sexo = input("Ingrese sexo (H/M): ").upper()
peso = float(input("Ingrese peso (kg): "))
altura = float(input("Ingrese altura (m): "))

# Objetos
persona1 = Persona(nombre, edad, sexo, peso, altura)
persona2 = Persona.constructor2(nombre, edad, sexo)
persona3 = Persona.constructorVacio()

personas = [persona1, persona2, persona3]

# Salida
for i, persona in enumerate(personas, start=1):
    print(f"\nPERSONA {i}")
    print(persona)

    imc = persona.calcularIMC()

    if imc == Persona.BAJO_PESO:
        print("Estado de peso: Bajo peso")
    elif imc == Persona.PESO_IDEAL:
        print("Estado de peso: Peso ideal")
    elif imc == Persona.SOBREPESO:
        print("Estado de peso: Sobrepeso")
    else:
        print("Estado de peso: No se puede calcular")

    if persona.esMayorDeEdad():
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
        
