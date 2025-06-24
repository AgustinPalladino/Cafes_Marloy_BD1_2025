from base_de_datos import conexion


def agregar_cliente(nombre, direccion, telefono, correo):
    try:
        cnx = conexion()
        cursor = cnx.cursor()
        query = "INSERT INTO clientes (nombre, direccion, telefono, correo) VALUES (%s, %s, %s, %s)" #%s para evitar injeccion y formatear correctamente los valores
        datos = (nombre, direccion, telefono, correo)
        cursor.execute(query, datos) #escribe la sentencia
        cnx.commit() #la ejecuta
        cnx.close() #cerramos la conexion
        return #evaluar si tiene que retornar un string o un booleano

    except Exception as error:
        return


def eliminar_cliente(id):
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
        return
    except Exception as error:
        return


def modificar_cliente(id, nombre, direccion, telefono, correo):
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
        return
    except Exception as error:
        return