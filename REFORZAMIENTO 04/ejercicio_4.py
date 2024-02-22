"""
Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
string = "Hello Pythonista"
print(string/0)
"""
def dividir_string():
    string = "Hello Pythonista"
    try:
        resultado = string / 0
        return resultado
    except TypeError as e:
        mensaje = "Error: No se puede realizar la operación de división con una cadena de texto."
        print(mensaje)
        print("Causa del error:", e)

dividir_string()
