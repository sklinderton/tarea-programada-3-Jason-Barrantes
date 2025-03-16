class Persona:
    def __init__(self, nombre, apellido1, apellido2, edad):
        self.__nombre = nombre
        self.__pellido1 = apellido1
        self.__apellido2 = apellido2
        self.__edad = edad

    def __str__(self):
        return f"{self.__nombre} {self.__pellido1} {self.__apellido2}, {self.__edad} años"