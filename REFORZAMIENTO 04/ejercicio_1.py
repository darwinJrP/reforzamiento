"""
1. Crear una función para encontrar el error en el siguiente bloque de
código. Crea una excepción para evitar que tu programa se bloquee y
además imprime un mensaje al usuario la causa y/o solución:
suma = 80 + “Hola Pythonista”
"""
def msj():
    try:
        suma = 80 + "Hola Pythonistas"
        return suma
    except TypeError as x:
        print("No se puede realizar la suma de datos distintos")
        print(f"Error: {x}")

msj()