''' Crea una lista vacía (con 10 posiciones), pedir al usuario c/u sus valores y que
finalmente se devuelva la suma y la media de los números ingresados de la lista. '''
lista_9 = []
print(f"La lista está vacia {lista_9}")
for i in range(1, 11):
    lista_9.append(float(input(f"Ingrese el valor #{i} para la lista_9:")))
print(f"Los valores de mi lista_9 son: {lista_9}")
suma_elementos = sum(lista_9)
print(f"La suma de los elementos de mi lista es: {suma_elementos} ")
media_elementos = suma_elementos/i
print(f"La media de los elementos de mi lista es: {media_elementos}")