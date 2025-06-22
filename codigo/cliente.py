from base_de_datos import conexion

cnx = conexion()
cursor = cnx.cursor() #traemos la conexion de la clase base_de_datos

def agregar_cliente(nombre, direccion, telefono, correo):
    query = "INSERT INTO clientes (nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s)" #%s para evitar injeccion y formatear correctamente los valores
    datos = (nombre, direccion, telefono, correo)
    cursor.execute(query, datos) #junta la sentencia
    cnx.commit() #la ejecuta


def eliminar_cliente(id):
    try:
        cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
        cliente = cursor.fetchone()

        if cliente is None:
            return

        cursor.execute("DELETE FROM clientes WHERE id = %s", (id,))
        cnx.commit()
    except Exception as e:
        return


def modificar_cliente(id, nombre, direccion, telefono, correo):
    try:
        query = "UPDATE clientes SET nombre = %S, direccion = %s, telefono = %s, correo = %s WHERE id = %s"

        cursor.execute(query, (nombre, direccion, telefono, correo, id))
        cnx.commit()
        return

    except Exception as e:
        return