import ejercicio_5

def main():
    nombre_usuario = input("Ingrese el nombre de usuario a validar: ")
    resultado = ejercicio_5.NombreUsuario(nombre_usuario)
    if resultado is True:
        print("El nombre de usuario es válido.")
    else:
        print(resultado)

if __name__ == "__main__":
    main()