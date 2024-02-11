"""
Escribir una clase en Python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico.
"""
class Calculadora:
    def __init__(self):
        self.resultado = None

    def pnum(self):
        numero = input("Ingrese un numero entero: ")
        while not numero.isdigit():
            numero = input("Ingrese un numero entero valido: ")
        return int(numero)

    def cubo(self, numero):
        self.resultado = numero**3

    def cuadrado_cubo(self):
        if self.resultado is None:
            print("Debe calcular el cubo primero.")
            return
        cuadrado_del_cubo = self.resultado**2
        print(cuadrado_del_cubo)

calc = Calculadora()
num = calc.pnum()
calc.cubo(num)
calc.cuadrado_cubo()





