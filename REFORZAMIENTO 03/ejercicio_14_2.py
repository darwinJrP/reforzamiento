import ejercicio_14

def main():
    nombre, apellido = ejercicio_14.ingresar_nombres_apellidos()
    print("Nombre completo:", nombre, apellido)

    tipo_seguro = ejercicio_14.pedir_tipo_seguro()
    print("Tipo de seguro:", tipo_seguro)

    ejercicio_14.es_mayor_de_edad()


if __name__ == "__main__":
    main()
