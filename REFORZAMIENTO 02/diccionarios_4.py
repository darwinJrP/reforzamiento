'''
Elimina el key edad tipo de tu diccionario, incluyendo su valor.

del var[‘key’]
'''
empleado = { "nombre": "Roy", "edad": 15, "salario": 1200, "edad para empleado": 18 }
empleado["dni"] = 74982192
del empleado["edad"]
print(empleado)