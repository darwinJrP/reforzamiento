"""
14. Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)
"""
def ingresar_nombres_apellidos():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    return nombre, apellido

def pedir_tipo_seguro():
    tipo_seguro = input("Ingrese el tipo de seguro: ")
    return tipo_seguro

def es_mayor_de_edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Es mayor de edad.")
    else:
        print("No es mayor de edad.")
