"""
Crear una clase en python que contenga un método que revierta una
cadena de palabras.
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seguimos Pythonista Hola"
Llamarlo mínimo 2 veces y mostrar el resultado por consola.
"""
class RevertidorCadena:
    @staticmethod
    def revertir_cadena(cadena):
        palabras = cadena.split()
        palabras.reverse()
        return ' '.join(palabras)

cadena1 = "Hola Pythonista, seguimos adelante"
resultado1 = RevertidorCadena.revertir_cadena(cadena1)
print("Input 1:", cadena1)
print("Output 1:", resultado1)

cadena2 = "¡Hola mundo!"
resultado2 = RevertidorCadena.revertir_cadena(cadena2)
print("Input 2:", cadena2)
print("Output 2:", resultado2)

