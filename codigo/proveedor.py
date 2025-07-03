from base_de_datos import conexion

def agregar_proveedor(nombre, contacto, usuario):
    if not nombre or not contacto:
        return "No se ha podido agregar el proveedor. Nombre y contacto no pueden estar vacios."

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO proveedores (nombre, contacto) VALUES (%s, %s)", (nombre, contacto))
        cnx.commit()
        cursor.close()
        cnx.close()
        return "Proveedor agregado correctamente."

    except Exception as error:
        return "No se ha podido agregar el proveedor. Error al agregar el proveedor."

def eliminar_proveedor(id, usuario):
    if not str(id).isdigit():
        return "No se ha podido eliminar el proveedor. El id debe ser numerico."

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM proveedores WHERE id = %s", (id,))
        prov = cursor.fetchone()
        if prov is None:
            if prov is None:
                return "No se ha podido eliminar el proveedor. No existe ese proveedor con esa ID"

        cursor.execute("DELETE FROM proveedores WHERE id = %s", (id,))
        cnx.commit()
        cnx.close()
        return "Proveedor eliminado correctamente."

    except Exception as error:
        return "No se ha podido eliminar el proveedor. Error al eliminar el proveedor."

def modificar_proveedor(id, nombre, contacto, usuario):
    if not str(id).isdigit():
        return "No se ha podido modificar el proveedor. El id debe ser numerico."
    if not nombre or not contacto:
        return "No se ha podido modificar el proveedor. Nombre y contacto no pueden estar vacios."

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM proveedores WHERE id = %s", (id,))
        prov = cursor.fetchone()
        if prov is None:
            return "No se ha podido modificar el proveedor. No existe ese proveedor con esa ID"

        cursor.execute("UPDATE proveedores SET nombre = %s, contacto = %s WHERE id = %s",
            (nombre, contacto, id))
        cnx.commit()
        cnx.close()
        return "Proveedor modificado correctamente."

    except Exception as error:
        return "No se ha podido modificar el proveedor. Error al modificar el proveedor."