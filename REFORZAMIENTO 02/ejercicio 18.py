'''
Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes
repetidos (los cuales son impares dentro del rango indicado y que no sea el último
impar).
- Empezando desde 1 y no 0.
- Agregar un cadena en la posición 3 de la lista.
- Eliminar este valor string de la cadena usando del.
'''
#Numeros impares, utilicé condicionales y el bucle for
lista_8 = []
for i in range (1,30):
    if i %2 != 0:
        lista_8.append(i)
print(f"Los valores de los primeros 15 impares son: {lista_8}")
for e in range (1,4):
    lista_8.append(1.1)
print(f"Los valores de mi lista actualizada, agregando 3 numeros flotantes repetidos son: {lista_8}")
lista_8.insert(3, "Lillia")
print(f"Los valores actualizados de mi lista, agregando una cadena en la posicion #3 de la lista son: {lista_8}")
del lista_8[3]
print(f"Los valores finales de mi lista, eliminando el valor en la posición #3 con la función 'del[]' son: {lista_8}")