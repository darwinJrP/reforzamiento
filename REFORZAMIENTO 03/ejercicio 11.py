"""
Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una
persona. Implementar los métodos necesarios para inicializar los
atributos (constructor), un método para mostrar los datos e indicar si
la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas.
"""

class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sueldo:", self.sueldo)

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} no es mayor de edad.")

    def bonificacion(self):
        bono = self.sueldo * 0.20
        print(f"Bonificación para {self.nombre}: {bono}")
        return bono


persona1 = Persona("Roy", 21, 1800)
persona2 = Persona("Lillia", 60, 1100)

print("Datos de la Persona 1:")
persona1.mostrar_datos()
persona1.es_mayor_de_edad()
persona1.bonificacion()
print()

print("Datos de la Persona 2:")
persona2.mostrar_datos()
persona2.es_mayor_de_edad()
persona2.bonificacion()
