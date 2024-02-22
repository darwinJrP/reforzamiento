import math

def cargar_entero():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("Error: Por favor ingrese un valor entero válido.")
        return None

def mostrar_raiz_cuadrada(valor):
    if valor is not None:
        print(f"La raíz cuadrada de {valor} es: {math.sqrt(valor)}")

def mostrar_cuadrado_y_cubo(valor):
    if valor is not None:
        print(f"El valor elevado al cuadrado es: {valor ** 2}")
        print(f"El valor elevado al cubo es: {valor ** 3}")
