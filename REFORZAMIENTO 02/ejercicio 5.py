''' Obten la cantidad total de ítems que tienes en tu lista creada y mostrar el  resultado
en consola. '''
lista_1 = ["Cálculo Multivariable", "Matemática Básica", "Lenguaje de programación para ingenieria",
           "Comunicación", "Cálculo Integral", "Ciencia y Tecnología de los Materiales"]
lista_1.append("Termodinamica")
lista_1.append("Física Molecular")
lista_1.append("Fundamentos de electricidad y magnetismo")
lista_1.append("Ecuaciones diferenciales")
lista_1.remove("Cálculo Multivariable")
lista_1.remove("Comunicación")
lista_1.reverse()
print(f"La cantidad de items en mi lista_1 son:", len(lista_1))