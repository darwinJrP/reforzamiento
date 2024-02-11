"""
Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, otro para imprimirlos y un método para mostrar un mensaje
con el resultado de la nota y si ha aprobado (mayor o igual a 11) o no el
alumno.Instanciar la clase por lo menos 3 veces (3 alumnos)
"""
class Alumno():
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimir(self):
        nombre = self.nombre
        edad = self.edad
        nota_final = self.nota_final
        return "Su nombre es:", nombre, "tiene", edad, "años y su nota final es", nota_final

    def estado(self):

        if self.nota_final < 11:

            print("Nota desaprobatoria")
        elif 11 <= self.nota_final <= 20:
            print("Aprobado")


alumno_1 = Alumno("Roy", 15, 14)
print(alumno_1.imprimir())
print(alumno_1.estado())

alumno_2 = Alumno("Kenny", 11, 20)
print(alumno_2.imprimir())
print(alumno_1.estado())









