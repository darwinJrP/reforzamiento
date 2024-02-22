"""
Haciendo el uso de *args y **kwargs aplicarlo debidamente para usar
decorar una función que recibirá 4 argumentos los cuales se
multiplicaran entre ellos.
Mensaje previo al usar el decorador “Está por ejecutarse la función” y
mensaje luego de usar el decorador “La función ha sido ejecutado
correctamente”
"""
def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función")
        resultado = funcion(*args, **kwargs)
        print("La función ha sido ejecutada correctamente")
        return resultado
    return wrapper

@decorador
def multiplicar(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

resultado = multiplicar(6, 7, 8, 9)
print("El resultado de la multiplicación es:", resultado)

