"""
Creando un archivo principal donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones.
- La primera función cargará una un número entero que pedirá al
usuario que ingrese por consola un valor.
- La segunda función solamente sumará dos valores.
- Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo
"""
import operaciones

def main():
    numero = operaciones.cargar_numero()
    if numero is not None:
        valor1 = numero
        valor2 = operaciones.cargar_numero()
        if valor2 is not None:
            resultado = operaciones.sumar_valores(valor1, valor2)
            print(f"La suma de {valor1} y {valor2} es: {resultado}")

if __name__ == "__main__":
    main()
