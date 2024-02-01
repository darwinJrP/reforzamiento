''' Borra el primer ítem de la lista usando debidamente su índice. '''
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
print(f"Los valores de mi lista_1 son: {lista_1}")
lista_1.pop(0)
print(f"Los valores de mi lista_1 actualizados son: {lista_1}")