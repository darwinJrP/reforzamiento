"""
Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion']
"""
def profesiones():
    persona = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
    try:
        e = persona['profesion']
        return e
    except KeyError as x:
        msj = "Error: La clave 'profesion' no existe en el diccionario."
        print(msj)
        print(f"Error: {x}")

profesiones()

