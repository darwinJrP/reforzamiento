"""
Crear una función que creará el archivo calificaciones.txt que contiene
las calificaciones de un curso.
Escribir un programa que contenga las siguientes funciones:
- Una función que guarde el nombre, 2 notas y el promedio (el
promedio lo calculará la función antes de escribirlo en el fichero)
- Y una función que leerá el fichero anterior y dirá si el alumno X,
aprobó o no, tener en cuenta que si tiene un promedio mayor a día
tendrá un mensaje de “Alumno X, aprobado” de lo contrario “Alumno
X, desaprobado”
"""


def guardar_calificacion(nombre, nota1, nota2):
    promedio = (nota1 + nota2) / 2

    with open("calificaciones.txt", "a") as archivo:
        archivo.write(f"{nombre},{nota1},{nota2},{promedio}\n")


def verificar_aprobacion(nombre_alumno):
    with open("calificaciones.txt", "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            partes = linea.strip().split(",")
            nombre = partes[0]
            promedio = float(partes[3])
            if nombre == nombre_alumno:
                if promedio >= 10:
                    return f"Alumno {nombre_alumno}, aprobado"
                else:
                    return f"Alumno {nombre_alumno}, desaprobado"
        return "Alumno no encontrado"


guardar_calificacion("Roy", 15, 18)
guardar_calificacion("Lillia", 8, 12)
guardar_calificacion("Darwin", 10, 11)

print(verificar_aprobacion("Juan"))
print(verificar_aprobacion("Lillia"))
print(verificar_aprobacion("Graves"))
print(verificar_aprobacion("Graves"))
