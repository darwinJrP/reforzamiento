"""
Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]
"""
def lista():
    lista_1 = [2, 6, 10, 4, 5, 23, 1]
    try:
        error_de_indice = lista_1[10]
        return error_de_indice
    except IndexError as x:
        msj = "Error: El índice está fuera del rango de la lista."
        print(msj)
        print("Error:", x)

lista()


