"""
Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:

- Una función que realizará la carga de un valor entero.
- Una función que mostrará por pantalla la raíz cuadrada de dicho
valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho
número.
- Utilizar el módulo math de python.
"""
import ejercicio_8_modulo

def main():
    valor = ejercicio_8_modulo.cargar_entero()
    ejercicio_8_modulo.mostrar_raiz_cuadrada(valor)
    ejercicio_8_modulo.mostrar_cuadrado_y_cubo(valor)

if __name__ == "__main__":
    main()
