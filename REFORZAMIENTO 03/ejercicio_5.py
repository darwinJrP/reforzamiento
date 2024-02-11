"""
Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados
por el usuario también y un segundo parámetro que eliminará de la
lista que fue ingresada a la función, finalmente el output de la función
será la lista actualizada sin el valor que se sacará de la lista. Mostrar
también la lista original y el número que fue eliminado.
"""


def eliminar_valor(lista, valor_eliminar):
    print("Lista original:", lista)
    print("Valor eliminado:", valor_eliminar)

    if valor_eliminar in lista:
        lista.remove(valor_eliminar)

    print("Lista actualizada:", lista)
    return lista


def main():
    valor1 = input("Ingrese el primer valor: ")
    valor2 = input("Ingrese el segundo valor: ")
    lista_usuario = input("Ingrese los valores de la lista: ").split(',')

    valor_eliminar = input("Ingrese el valor a eliminar de la lista: ")

    eliminar_valor(lista_usuario, valor_eliminar)

if __name__ == "__main__":
    main()
