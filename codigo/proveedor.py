from base_de_datos import conexion

def agregar_proveedor(nombre, contacto, usuario):
    if not usuario[1]: #si no es admin no puede agregar
        return {"exito": False, "mensaje": "Permiso rechazado, necesita ser administrador."}
    if not nombre or not contacto:
        return {"exito": False, "mensaje": "Nombre y contacto no pueden estar vacios."}

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("insert into proveedores (nombre, contacto) values (%s, %s)", (nombre, contacto))
        cnx.commit()
        cursor.close()
        cnx.close()
        return {"exito:": True, "mensaje": "Proveedor agregado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al agregar el proveedor."}

def eliminar_proveedor(id, usuario):
    if not usuario[1]:
        return {"exito": False, "mensaje": "Permiso rechazado, necesita ser administrador."}
    if not str(id).isdigit():
        return {"exito": False, "mensaje": "El id debe ser numerico."}

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("select * from proveedores where id = %s", (id,))
        prov = cursor.fetchone()
        if prov is None:
            if prov is None:
                return {"exito": False, "mensaje": "No existe ese proveedor con esa ID"}

        cursor.execute("delete from proveedores where id = %s", (id,))
        cnx.commit()
        cnx.close()
        return {"exito:": True, "mensaje": "Proveedor eliminado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al eliminar el proveedor."}

def modificar_proveedor(id, nombre, contacto, usuario):
    if not usuario[1]:
        return {"exito": False, "mensaje": "Permiso rechazado, necesita ser administrador."}
    if not str(id).isdigit():
        return {"exito": False, "mensaje": "El id debe ser numerico."}
    if not nombre or not contacto:
        return {"exito": False, "mensaje": "Nombre y contacto no pueden estar vacios."}

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("select * from proveedores where id = %s", (id,))
        prov = cursor.fetchone()
        if prov is None:
            return {"exito": False, "mensaje": "No existe ese proveedor con esa ID"}

        cursor.execute("UPDATE proveedores SET nombre = %s, contacto = %s WHERE id = %s",
            (nombre, contacto, id))
        cnx.commit()
        cnx.close()
        return {"exito:": True, "mensaje": "Proveedor modificado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al modificar el proveedor."}