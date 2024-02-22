"""
Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:
- Una función que genere 30 números enteros aleatorios entre 0 y
100, que muestre en pantalla esta lista.
- Otra función que ordene los valores de una lista y volver a
mostrarla.
"""
import ejercicio_7_modulo

numeros_aleatorios = ejercicio_7_modulo.generar_numeros_aleatorios()

lista_ordenada = ejercicio_7_modulo.ordenar_lista(numeros_aleatorios)
