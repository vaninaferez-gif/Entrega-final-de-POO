import random
import string


class Password:

    def __init__(self, longitud=8):
        self.__longitud = longitud
        self.__contraseña = ""
        self.generar_password()

    def es_fuerte(self):

        mayusculas = 0
        minusculas = 0
        numeros = 0

        for caracter in self.__contraseña:

            if caracter.isupper():
                mayusculas += 1

            elif caracter.islower():
                minusculas += 1

            elif caracter.isdigit():
                numeros += 1

        return mayusculas > 2 and minusculas > 1 and numeros > 5

    def generar_password(self):

        caracteres = string.ascii_letters + string.digits

        contraseña = ""

        for i in range(self.__longitud):
            contraseña += random.choice(caracteres)

        self.__contraseña = contraseña

    # Getters
    def get_contraseña(self):
        return self.__contraseña

    def get_longitud(self):
        return self.__longitud

    # Setter
    def set_longitud(self, longitud):
        self.__longitud = longitud
