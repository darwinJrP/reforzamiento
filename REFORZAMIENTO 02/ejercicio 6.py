'''
Devuelve la cantidad de veces que se repite un curso (agregarla previamente a la lista)
dentro de la lista.
'''
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
print(f"La cantidad de veces que se repite 'Comunicación' en mi lista_1 es:", lista_1.count("Comunicación") )

