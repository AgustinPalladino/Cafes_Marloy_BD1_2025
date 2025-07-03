from base_de_datos import conexion
import re



def agregar_cliente(nombre, direccion, telefono, correo):
    if not all([nombre, direccion, telefono, correo]):
        return "No se ha podido agregar el cliente. Todos los campos son necesarios."
    if not telefono.isdigit():
        return "No se ha podido agregar el cliente. El teléfono debe contener solo números."
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
        return "No se ha podido agregar el cliente. Correo invalido."

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        query = "INSERT INTO clientes (nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s)" #%s para evitar injeccion y formatear correctamente los valores
        datos = (nombre, direccion, telefono, correo)
        cursor.execute(query, datos) #escribe la sentencia
        cnx.commit() #la ejecuta
        cnx.close() #cerramos la conexion
        return "Cliente agregado correctamente."

    except Exception as error:
        return "No se ha podido agregar el cliente. Error al agregar el cliente."


def eliminar_cliente(id):
    if not str(id).isdigit():
        return "No se ha podido eliminar el cliente. ID invalido."

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        clnte = cursor.fetchone()

        if clnte is None:
            return

        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        cnx.commit()
        cnx.close()
        return "Cliente eliminado correctamente."
    except Exception as error:
        return "No se ha podido eliminar el cliente. Error al eliminar el cliente."


def modificar_cliente(id, nombre, direccion, telefono, correo):
    if not str(id).isdigit():
        return "No se ha podido modificar el cliente. ID invalido."
    if not all([nombre, direccion, telefono, correo]):
        return "No se ha podido modificar el cliente. Todos los campos son obligatorios."
    if not telefono.isdigit():
        return "No se ha podido modificar el cliente. El teléfono debe contener solo números."
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
        return "No se ha podido modificar el cliente. Correo invalido."

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        clnte = cursor.fetchone()

        if clnte is None:
            return

        query = "UPDATE clientes SET nombre = %s, direccion = %s, telefono = %s, correo = %s WHERE id = %s"
        cursor.execute(query, (nombre, direccion, telefono, correo, id))
        cnx.commit()
        cnx.close()
        return "Cliente modificado correctamente."
    except Exception as error:
        return "No se ha podido modificar el cliente. Error al modificar el cliente."