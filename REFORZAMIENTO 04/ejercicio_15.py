"""
Queremos consumir un JSON que se encuentra alojado en la nube el cual
nos traerá los datos de una persona como la edad, nombre, email, dirección
o nombre de la compañía en donde trabaja.
La url a consumir usando Python es la siguiente:

https://jsonplaceholder.typicode.com/users

Obtener respectivamente los valores necesarios para formar la siguiente
oración:

Bienvenido “nombre” “apellido”, usted tiene “edad” años. El correo que
nos proporcionó es “correo” y la compañía actual donde trabaja se llama
“nombreCompañía”. Dentro de sus datos también encontramos una website
que es: “nombreWeb”

Finalmente agregar un usuario al json obtenido pero sólo con los datos de
nombre, apellido, edad y compañía donde trabaja y finalmente mostrarlo en
consola (sólo ese usuario nuevo)
"""
import urllib.request
import json

# Obtener el JSON de la URL
url = "https://jsonplaceholder.typicode.com/users"
response = urllib.request.urlopen(url)
data = json.loads(response.read())

# Iterar sobre cada usuario en el JSON
for user in data:
    nombre = user["name"].split()[0]
    apellido = user["name"].split()[1]
    email = user["email"]
    nombreCompañia = user["company"]["name"]
    direccion = user["address"]["street"]
    nombreWeb = user["website"]

    # Mensaje
    oracion = f"Bienvenido {nombre} {apellido}, su correo electrónico es {email}. Trabaja en la compañía llamada {nombreCompañia}. Vive en {direccion}. Su sitio web es: {nombreWeb}"

    print(oracion)

# Nuevo usuario
nuevo_usuario = {
    "name": "Nuevo Usuario",
    "email": "nuevo@usuario.com",
    "company": {
        "name": "Nueva Compañía"
    },
    "address": {
        "street": "Calle Nueva 123"
    },
    "website": "www.nuevousuario.com"
}

# Agregar el nuevo usuario al JSON
data.append(nuevo_usuario)

# Mostrar solo el nuevo usuario en la consola
print(data[-1])

