"""
12. Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:

Añadir contacto
Mostrar contactos
Buscar contacto
(Por DNI)
"""
class Agenda:
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email, dni):
        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "dni": dni
        }
        self.contactos.append(contacto)
        print("Se añadio el contacto")

    def mostrar_contactos(self):
        if self.contactos:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(contacto)
        else:
            print("La agenda está vacía.")

    def buscar_contacto(self, dni):
        for contacto in self.contactos:
            if contacto["dni"] == dni:
                print("Contacto encontrado:")
                print(contacto)
                return
        print("Contacto inválido")

agenda = Agenda()

agenda.añadir_contacto("Roy", "123456666", "roy22@renanmail.com", "74455593")
agenda.añadir_contacto("X", "977444555", "maria@joemail.com", "74992200")

agenda.mostrar_contactos()

agenda.buscar_contacto("74455593")
agenda.buscar_contacto("99999999X")
