''' 4.Hallar el volumen de una esfera, cada dato requerido para hallar el volumen debe
estar en una variable. Mostrar el volumen por pantalla. '''
radio_esfera = int(input("Ingrese el radio de la esfera: "))
numero_pi = 3.141592
volumen_esfera = 4*numero_pi*(radio_esfera**3)
print(f"El volumen de la esfera es: {volumen_esfera}")
''' No utilicé la libreria o el import math para el numero pi, cabe aclarar que la potencia también 
se pudo realizar con un 'pow()' '''