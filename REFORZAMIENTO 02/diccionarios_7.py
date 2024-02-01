"""
 Crear un diccionario con 6 departamentos en el país.
➢ Borrar cualquier departamento (uno) usando la palabra reservada del.
➢ Comprobar que no existe este departamento borrado dentro del diccionario.
"""
departamentos = { "Departamento_1":"Lima", "Departamento_2":"Tacna", "Departamento_3":"Arequipa", "Departamento_4":"Ucayali", "Departamento_5":"Iquitos", "Departamento_6":"Huánuco"}
print(departamentos)
del departamentos["Departamento_1"]
print(departamentos)