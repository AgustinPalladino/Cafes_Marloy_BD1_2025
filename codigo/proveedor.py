from base_de_datos import conexion

def agregar_proveedor(nombre, contacto, usuario):
    if not usuario[1]: # si no es admin no puede agregar proveedores
        return

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("insert into proveedores (nombre, contacto) values (%s, %s)", (nombre, contacto))
        cnx.commit()
        cursor.close()
        cnx.close()
        return

    except Exception as error:
        return

def eliminar_proveedor(id, usuario):
    if not usuario[1]:
        return

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("select * from proveedores where id = %s", (id,))
        prov = cursor.fetchone()
        if prov is None:
            return

        cursor.execute("delete from proveedores where id = %s", (id,))
        cnx.commit()
        cnx.close()
        return

    except Exception as error:
        return

def modificar_proveedor(id, nombre, contacto, usuario):
    if not usuario[1]:
        return

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("select * from proveedores where id = %s", (id,))
        prov = cursor.fetchone()
        if prov is None:
            return

        cursor.execute("UPDATE proveedores SET nombre = %s, contacto = %s WHERE id = %s",
            (nombre, contacto, id))
        cnx.commit()
        cnx.close()
        return

    except Exception as error:
        return