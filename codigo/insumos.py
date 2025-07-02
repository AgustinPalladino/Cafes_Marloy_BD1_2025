from base_de_datos import conexion

def agregar_insumo(descripcion, tipo, precioUnitario, id_proveedor):
    if not all([descripcion, tipo, precioUnitario, id_proveedor]):
        return {"exito": False, "mensaje": "Todos los campos son necesarios."}
    if not precioUnitario > 0:
        return {"exito": False, "mensaje": "El precio debe ser un numero positivo."}
    if not str(id_proveedor).isdigit():
        return {"exito": False, "mensaje": "El id del proveedor debe ser numerico."}

    try:
        cnx = conexion()
        cursor = cnx.cursor() #traemos la conexion de la clase base_de_datos
        query = "INSERT INTO insumos (descripcion, tipo, precioUnitario, idProveedor) VALUES (%s, %s, %s, %s)" #%s para evitar injeccion y formatear correctamente los valores
        datos = (descripcion, tipo, precioUnitario, id_proveedor)
        cursor.execute(query, datos) #junta la sentencia
        cnx.commit() #la ejecuta
        cnx.close()
        return {"exito": True, "mensaje": "Insumo agregado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al agregar el insumo."}


def eliminar_insumo(id):
    if not str(id).isdigit():
        return {"exito": False, "mensaje": "ID invalido."}

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
        return {"exito:": True, "mensaje": "Insumo eliminado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al eliminar el insumo."}


def modificar_insumo(id, descripcion, tipo, precioUnitario, id_proveedor):
    if not all([descripcion, tipo, precioUnitario, id_proveedor]):
        return {"exito": False, "mensaje": "Todos los campos son necesarios."}
    if not str(id).isdigit():
        return {"exito": False, "mensaje": "ID invalido."}
    if not precioUnitario > 0:
        return {"exito": False, "mensaje": "El precio debe ser un numero positivo."}
    if not str(id_proveedor).isdigit():
        return {"exito": False, "mensaje": "El id del proveedor debe ser numerico."}


    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM insumos WHERE id = %s", (id,))
        insum = cursor.fetchone()
        if insum is None:
            return {"exito": False, "mensaje": "No existe insumo con esa ID"}

        query = "UPDATE insumos SET descripcion = %s, tipo = %s, precioUnitario = %s, idProveedor = %s WHERE id = %s"
        cursor.execute(query, (descripcion, tipo, precioUnitario, id_proveedor, id))
        cnx.commit()
        cnx.close()
        return {"exito:": True, "mensaje": "Insumo modificado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al modificar el insumo."}