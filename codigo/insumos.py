from base_de_datos import conexion

def agregar_insumo(descripcion, tipo, precioUnitario, id_proveedor):
    if not all([descripcion, tipo, precioUnitario, id_proveedor]):
        return "No se ha podido agregar el insumo. Todos los campos son necesarios."
    if not precioUnitario > 0:
        return "No se ha podido agregar el insumo. El precio debe ser un numero positivo."
    if not str(id_proveedor).isdigit():
        return "No se ha podido agregar el insumo. El id del proveedor debe ser numerico."

    try:
        cnx = conexion()
        cursor = cnx.cursor() #traemos la conexion de la clase base_de_datos
        query = "INSERT INTO insumos (descripcion, tipo, precioUnitario, idProveedor) VALUES (%s, %s, %s, %s)" #%s para evitar injeccion y formatear correctamente los valores
        datos = (descripcion, tipo, precioUnitario, id_proveedor)
        cursor.execute(query, datos) #junta la sentencia
        cnx.commit() #la ejecuta
        cnx.close()
        return "Insumo agregado correctamente."

    except Exception as error:
        return "No se ha podido agregar el insumo. Error al agregar el insumo."


def eliminar_insumo(id):
    if not str(id).isdigit():
        return "No se ha podido eliminar el insumo. ID invalido."

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM insumos WHERE id = %s", (id,))
        insum = cursor.fetchone()
        if insum is None:
            return "No se ha podido eliminar el insumo. no existe insumo con esa ID."

        cursor.execute("DELETE FROM insumos WHERE id = %s", (id,))
        cnx.commit()
        cnx.close()
        return "Insumo eliminado correctamente."

    except Exception as error:
        return "No se ha podido eliminar el insumo. Error al eliminar el insumo."


def modificar_insumo(id, descripcion, tipo, precioUnitario, id_proveedor):
    if not all([descripcion, tipo, precioUnitario, id_proveedor]):
        return "No se ha podido modificar el insumo. Todos los campos son necesarios."
    if not str(id).isdigit():
        return "No se ha podido modificar el insumo. ID invalido."
    if not precioUnitario > 0:
        return "No se ha podido modificar el insumo. El precio debe ser un numero positivo."
    if not str(id_proveedor).isdigit():
        return "No se ha podido modificar el insumo. El id del proveedor debe ser numerico."


    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM insumos WHERE id = %s", (id,))
        insum = cursor.fetchone()
        if insum is None:
            return "No se ha podido modificar el insumo. No existe insumo con esa ID."

        query = "UPDATE insumos SET descripcion = %s, tipo = %s, precioUnitario = %s, idProveedor = %s WHERE id = %s"
        cursor.execute(query, (descripcion, tipo, precioUnitario, id_proveedor, id))
        cnx.commit()
        cnx.close()
        return "Insumo modificado correctamente."

    except Exception as error:
        return "No se ha podido modificar el insumo. Error al modificar el insumo."