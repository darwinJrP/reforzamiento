""" Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la
función una vez y mostrar el resultado por consola). Los números
serán ingresados y solicitados al usuario."""

var_1 = int(input("Ingrese el primer numero: "))
var_2 = int(input("Ingrese el segundo numero: "))
def cuadrados(a,b):
    for i in range(a,b+1):
        cuadrado_numeros = print(pow(i,2))
    return cuadrado_numeros

print(cuadrados(var_1,var_2))