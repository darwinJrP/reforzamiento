""" Pedir al usuario que ingrese una oración con un mínimo de 3 palabras
la cual será usada por parámetro para una función que se creará e
indicará cuantas palabras existen dentro de la oración ingresada. """

oracion = str(input("Ingrese una oración(como mínimo de 3 palabras): "))

oracion_separacion = oracion.split()

print(f"La cantidad de palabras de mi oración es: {len(oracion_separacion)}")

while(len(oracion_separacion) < 3):
    print("¡Ingrese una oración como mínimo de 3 palabras!")
    oracion = str(input("Vuelva a ingresar la oracion: "))
    oracion_separacion = oracion.split()


def palabras_oracion(i):
    palabras = i.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

cantidad_palabras = palabras_oracion(oracion)
print(cantidad_palabras)


