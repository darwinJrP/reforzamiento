''' 8.Usando la condicional if imprimir por pantalla si una lista está vacía o no, probar con
una lista vacía y otra con una lista no vacía.'''
lista_1 = []
print(lista_1)
if lista_1 == []:
    print("Lista vacía")
lista_1.append("Hi")
print(f"El nuevo valor de mi lista es: {lista_1}")
if lista_1 == []:
    print("Lista vacía")
else:
    print("Lista no vacía")