""" Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los
números cuya sumatoria de dígitos es menor que 10. Utilizar una o
más funciones, según sea conveniente. """

var_1 = int(input("Ingrese el dato #1: "))

while (var_1 <= 0):
    var_1 = int(input("Vuelva a ingresar el dato #1: "))

var_2 = int(input("Ingrese el dato #2: "))

while (var_2 <= 0):
    var_2 = int(input("Vuelva a ingresar el dato #2: "))


#Declarando la función que sumará los digitos
def sumatoria_digitos(a):
    suma_digitos = 0
    a_string = str(a)
    for digitos in a_string:
        suma_digitos = suma_digitos + int(digitos)
    return suma_digitos

#Evaluando var_1 y var_2 en la función creada ('def sumatoria_digitos(a)')
suma_digitos1 = sumatoria_digitos(var_1)
suma_digitos2 = sumatoria_digitos(var_2)

if suma_digitos1 < 10:
    print(var_1)
if  suma_digitos2 < 10:
    print(var_2)


if suma_digitos1 > suma_digitos2:
    print(f"El número cuya sumatoria de digitos es mayor: {var_1}")
elif suma_digitos2 > suma_digitos1:
    print(f" El número cuya sumatoria de digitos es mayor: {var_2}")
else:
    print("La sumatoria de digitos de los dos números son iguales.")











