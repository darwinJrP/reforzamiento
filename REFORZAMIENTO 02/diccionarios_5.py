# Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tiene.
empleado = { "nombre": "Roy", "edad": 15, "salario": 1200, "edad para empleado": 18 }
empleado["dni"] = 74982192
del empleado["edad"]
lista = list(empleado)
print(f"Mi diccionario convertido es el siguiente: {lista}")
print(type(lista))