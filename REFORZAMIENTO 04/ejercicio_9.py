"""
Crear una función que pida al usuario un número entero entre 1 y 20 y
guarde en un fichero (que no existe) con el nombre tabla.txt la tabla
de multiplicar de ese número, done n es el número introducido.
"""
def tabla_multiplicar(numero):
    if numero < 1 or numero > 20:
        print("El número debe estar entre 1 y 20.")
        return

    with open("tabla.txt", "w") as archivo:
        archivo.write(f"Tabla de multiplicar del {numero}:\n")
        for i in range(1, 11):
            resultado = numero * i
            archivo.write(f"{numero} x {i} = {resultado}\n")


numero_usuario = int(input("Por favor, introduce un número entero entre 1 y 20: "))
tabla_multiplicar(numero_usuario)
