""" Crear una función que sume los dígitos del número ingresado y
muestre por consola la suma de estos dígitos. """

var_1 = int(input("Digite un numero: "))

def sumadigitos(a):
    an = 0
    numero_str = str(a)
    for i in numero_str:
        an = an + int(i)
    return an

suma_de_digitos = sumadigitos(var_1)
print(f"La suma de los digitos del número ingresado es: {suma_de_digitos}")


