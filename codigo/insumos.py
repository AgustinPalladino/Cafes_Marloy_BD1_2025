from base_de_datos import conexion

def agregar_insumo(descripcion, tipo, precioUnitario, id_proveedor):
    try:
        cnx = conexion()
        cursor = cnx.cursor() #traemos la conexion de la clase base_de_datos
        query = "INSERT INTO insumos (descripcion, tipo, precioUnitario, idProveedor) VALUES (%s, %s, %s, %s)" #%s para evitar injeccion y formatear correctamente los valores
        datos = (descripcion, tipo, precioUnitario, id_proveedor)
        cursor.execute(query, datos) #junta la sentencia
        cnx.commit() #la ejecuta
        cnx.close()
        return

    except Exception as error:
        return


def eliminar_insumo(id):
    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM insumos WHERE id = %s", (id,))
        insum = cursor.fetchone()
        if insum is None:
            return

        cursor.execute("DELETE FROM insumos WHERE id = %s", (id,))
        cnx.commit()
        cnx.close()
        return

    except Exception as error:
        return


def modificar_insumo(id, descripcion, tipo, precioUnitario, id_proveedor):
    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM insumos WHERE id = %s", (id,))
        insum = cursor.fetchone()
        if insum is None:
            return

        query = "UPDATE insumos SET descripcion = %s, tipo = %s, precioUnitario = %s, idProveedor = %s WHERE id = %s"
        cursor.execute(query, (descripcion, tipo, precioUnitario, id_proveedor, id))
        cnx.commit()
        cnx.close()
        return

    except Exception as error:
        return