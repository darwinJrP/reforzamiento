''' Quita 2 elementos de tu nueva lista ítems por valor, no por índice. '''
lista_1 = ["Cálculo Multivariable", "Matemática Básica", "Lenguaje de programación para ingenieria",
           "Comunicación", "Cálculo Integral", "Ciencia y Tecnología de los Materiales"]
lista_1.append("Termodinamica")
lista_1.append("Física Molecular")
lista_1.append("Fundamentos de electricidad y magnetismo")
lista_1.append("Ecuaciones diferenciales")
print(f"Los antiguos valores de mi lista_1 son: {lista_1}")
lista_1.remove("Cálculo Multivariable")
lista_1.remove("Comunicación")
print(f"Los nuevos valores de mi lista_1 son: {lista_1}")