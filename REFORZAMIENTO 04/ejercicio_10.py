"""
Crear una función donde se permitirá guardar el nombre, apellido y
edad de un usuario en un fichero (agenda.txt), cada usuario tiene que
estar guardado en una línea diferente y cada dato de una persona tiene
que estar separados por comas.
"""
def agregar_usuario(nombre, apellido, edad):

    with open("agenda.txt", "a") as archivo:
        archivo.write(f"{nombre},{apellido},{edad}\n")

nombre = input("Introduce el nombre del usuario: ")
apellido = input("Introduce el apellido del usuario: ")
edad = input("Introduce la edad del usuario: ")

agregar_usuario(nombre, apellido, edad)
