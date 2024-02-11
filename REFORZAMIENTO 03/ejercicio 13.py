"""
Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase
Persona y agregue un atributo sueldo y muestre si debe pagar
impuestos (10% de su sueldo-encapsulamiento) (sueldo superior a
4000)
Instanciar la clase Empleado, mostrar el sueldo del empleado y cuánto
debe pagar de impuesto.
"""
class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))

    def impuesto(self):
        impuesto = 0
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.10
        return impuesto

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sueldo: {self.sueldo}")
        impuesto = self.calcular_impuesto()
        print(f"Impuesto a pagar: {impuesto}")

empleado = Empleado()
empleado.mostrar()
