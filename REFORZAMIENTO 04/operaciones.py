def cargar_numero():
    try:
        numero = int(input("Ingrese un número entero: "))
        return numero
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")

def sumar_valores(valor1, valor2):
    return valor1 + valor2
