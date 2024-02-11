"""
Crear una clase que contenga dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados, pero estarán contenidos en un diccionario.
Comprobar ambos métodos instanciado la clase respectivamente.
Considerar en el constructor los valores necesarios.
"""
class Persona:

    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.edad = None


    def ingresar_nombre_y_apellido(self):
        self.nombre = str(input("Ingrese nombre: "))
        self.apellido = str(input("Ingrese su apellido: "))


    def ingresar_edad(self):
        self.edad = int(input("Ingrese su edad: "))
        while self.edad < 0:
            self.edad = int(input("Vuelva a ingresar su edad: "))


    def imprimir(self):
        diccionario = {"nombre": self.nombre, "apellido": self.apellido,"edad": self.edad}
        print(f"Los valores de mi diccionario son: {diccionario}")

persona = Persona
persona.ingresar_nombre_y_apellido(persona)
persona.ingresar_edad(persona)
persona.imprimir(persona)