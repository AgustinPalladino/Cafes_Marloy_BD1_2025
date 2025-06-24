from base_de_datos import conexion

def agregar_tecnico(ci, nombre, apellido, telefono, usuario):
    if not usuario[1]: # si no es admin no puede agregar proveedores
        return

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("insert into tecnicos (ci, nombre, apellido, telefono) values (%s, %s, %s, %s)",
                       (ci,nombre, apellido, telefono))
        cnx.commit()
        cursor.close()
        cnx.close()
        return

    except Exception as error:
        return

def eliminar_tecnico(ci, usuario):
    if not usuario[1]:
        return

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("select * from tecnicos where ci = %s", (ci,))
        prov = cursor.fetchone()
        if prov is None:
            return

        cursor.execute("delete from tecnicos where ci = %s", (ci,))
        cnx.commit()
        cnx.close()
        return

    except Exception as error:
        return

def modificar_tecnico(ci, nombre, apellido, telefono, usuario):
    if not usuario[1]:
        return

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("select * from tecnicos where ci = %s", (ci,))
        prov = cursor.fetchone()
        if prov is None:
            return

        cursor.execute("UPDATE tecnicos SET nombre = %s, apellido = %s, telefono = %s WHERE ci = %s",
            (nombre, apellido, telefono, ci))
        cnx.commit()
        cnx.close()
        return

    except Exception as error:
        return