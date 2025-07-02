from base_de_datos import conexion
import re



def agregar_cliente(nombre, direccion, telefono, correo):
    if not all([nombre, direccion, telefono, correo]):
        return {"exito": False, "mensaje": "Todos los campos son necesarios."}
    if not telefono.isdigit():
        return {"exito": False, "mensaje": "El teléfono debe contener solo números."}
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
        return {"exito": False, "mensaje": "Correo invalido"}

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        query = "INSERT INTO clientes (nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s)" #%s para evitar injeccion y formatear correctamente los valores
        datos = (nombre, direccion, telefono, correo)
        cursor.execute(query, datos) #escribe la sentencia
        cnx.commit() #la ejecuta
        cnx.close() #cerramos la conexion
        return {"exito:": True, "mensaje": "Cliente agregado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al agregar el cliente."}


def eliminar_cliente(id):
    if not str(id).isdigit():
        return {"exito": False, "mensaje": "ID invalido."}

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
        return {"exito: ": True, "mensaje": "Cliente eliminado correctamente."}
    except Exception as error:
        return {"exito": False, "mensaje": "Error al eliminar el cliente."}


def modificar_cliente(id, nombre, direccion, telefono, correo):
    if not str(id).isdigit():
        return {"exito": False, "mensaje": "ID invalido."}
    if not all([nombre, direccion, telefono, correo]):
        return {"exito": False, "mensaje": "Todos los campos son obligatorios."}
    if not telefono.isdigit():
        return {"exito": False, "mensaje": "El teléfono debe contener solo números."}
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
        return {"exito": False, "mensaje": "Correo invalido"}

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
        return {"exito:": True, "mensaje": "Cliente modificado correctamente."}
    except Exception as error:
        return {"exito": False, "mensaje": "Error al modificar el cliente."}