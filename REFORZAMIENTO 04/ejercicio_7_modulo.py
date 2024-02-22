import random

def generar_numeros_aleatorios():
    numeros_aleatorios = [random.randint(0, 100) for _ in range(30)]
    print("Lista de números enteros aleatorios entre 0 y 100:")
    print(numeros_aleatorios)
    return numeros_aleatorios

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    print(lista_ordenada)
    return lista_ordenada
