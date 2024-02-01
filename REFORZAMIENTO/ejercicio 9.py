''' 9.Elevar al exponente de 4 un número que su valor estará asignado a una variable y
luego restar este mismo valor multiplicado por dos (usar pow). Mostrar el resultado en
pantalla. '''
var_1 = float(input("Ingrese un dato numérico: "))
var_exponente = pow(var_1,4)
print(f"Mi valor elevado al exponente 4 es: {var_exponente}")
resta_valor = var_1 * 2
operacion = var_exponente - resta_valor
print(f"El resultado de restar la potencia con el mismo valor ingresado multiplicado por dos es: {operacion}")