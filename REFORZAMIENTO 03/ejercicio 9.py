"""
Crear una clase llamada círculo que contenga radio en su constructory
que contenga un método área que devuelva el área de un círculo.
Aplicar excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.
Instanciar la clase respectivamente para dos diferentes radios.
Habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola.
"""
class Circulo:
    def __init__(self,radio):
        self.radio = radio

    def ingrese_radio(self):
        self.radio = float(input("Ingrese el radio del circulo: "))

    def area(self):
        area_circulo = 3.1415* pow(self.radio,2)
        print("El area del circulo es: ", area_circulo, "metros cuadrados")

    def perimetro(self):
        perimetro_circulo = 2* 3.1415 * self.radio
        print("El perimetro del circulo es: ", perimetro_circulo, "metros")

#INSTANCIANDO PRIMER VALOR
circulo_1 = Circulo
circulo_1.ingrese_radio(circulo_1)
circulo_1.area(circulo_1)
circulo_1.perimetro(circulo_1)

#SEGUNDO VALOR
circulo_2 = Circulo
circulo_2.ingrese_radio(circulo_2)
circulo_2.area(circulo_2)
circulo_2.perimetro(circulo_2)

