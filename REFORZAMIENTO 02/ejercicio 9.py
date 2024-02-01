''' Sumar las dos listas creadas anteriormente y mostrar el resultado en terminal. '''
#LISTA 1
lista_1 = ["Cálculo Multivariable", "Matemática Básica", "Lenguaje de programación para ingenieria",
           "Comunicación", "Cálculo Integral", "Ciencia y Tecnología de los Materiales"]
lista_1.append("Termodinamica")
lista_1.append("Física Molecular")
lista_1.append("Fundamentos de electricidad y magnetismo")
lista_1.append("Ecuaciones diferenciales")
lista_1.remove("Cálculo Multivariable")
lista_1.remove("Comunicación")
lista_1.reverse()
lista_1.append("Comunicación")
lista_1.append("Comunicación")
lista_1.append("Comunicación")
lista_1.pop(0)
#LISTA 2
lista_2 = []
lista_2.append(2.1)
lista_2.append(3.141592)
lista_2.append(0.26)
lista_2.append(1)
lista_2.append(2)
lista_2.append(3)
lista_2.append("Hi")
lista_2.append("Lillia")
lista_2.append("Diamond")

#Declaramos la variable suma
suma_de_listas = lista_1 + lista_2
print(f"Los valores obtenidos al sumar las dos listas son: {suma_de_listas}")