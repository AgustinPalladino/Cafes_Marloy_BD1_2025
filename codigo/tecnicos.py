from base_de_datos import conexion

def agregar_tecnico(ci, nombre, apellido, telefono, usuario):
    if not str(ci).isdigit():
        return "No se ha podido agregar el tecnico. La cedula debe ser solo numeros, sin puntos, ni guiones."
    if not telefono or not str(telefono).isdigit():
        return "No se ha podido agregar el tecnico. El telefono debe contener solo numeros."
    if not nombre or not apellido:
        return "No se ha podido agregar el tecnico. Nombre y apellidos vacios"

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO tecnicos (ci, nombre, apellido, telefono) VALUES (%s, %s, %s, %s)",
                       (ci,nombre, apellido, telefono))
        cnx.commit()
        cursor.close()
        cnx.close()
        return "Tecnico agregado correctamente."

    except Exception as error:
        return "No se ha podido agregar el tecnico. Error al agregar el tecnico."


def eliminar_tecnico(ci, usuario):
    if not str(ci).isdigit():
        return "No se ha podido eliminar el tecnico. La cedula debe ser solo numeros, sin puntos, ni guiones."

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM tecnicos WHERE ci = %s", (ci,))
        tec = cursor.fetchone()
        if tec is None:
            return "No se ha podido eliminar el tecnico. No existe ese tecnico con esa cedula"
        
        cursor.execute("SELECT COUNT(*) FROM mantenimientos WHERE ciTecnico = %s", (ci,))
        cantidad = cursor.fetchone()[0] 
        if cantidad > 0:
            return "No se ha podido eliminar el tecnico. El técnico tiene mantenimientos asignados y no puede ser eliminado."

        cursor.execute("DELETE FROM tecnicos WHERE ci = %s", (ci,))
        cnx.commit()
        cnx.close()
        return "Tecnico eliminado correctamente."

    except Exception as error:
        return "No se ha podido eliminar el tecnico. Error al eliminar el tecnico."

def modificar_tecnico(ci, nombre, apellido, telefono, usuario):
    if not str(ci).isdigit():
        return "No se ha podido modificar el tecnico. La cedula debe ser solo numeros, sin puntos, ni guiones."
    if not telefono or not str(telefono).isdigit():
        return "No se ha podido modificar el tecnico. El telefono debe contener solo numeros."
    if not nombre or not apellido:
        return "No se ha podido modificar el tecnico. Nombre y apellidos vacios"

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM tecnicos WHERE ci = %s", (ci,))
        tec = cursor.fetchone()
        if tec is None:
            return "No se ha podido modificar el tecnico. No existe ese tecnico con esa cedula"

        cursor.execute("UPDATE tecnicos SET nombre = %s, apellido = %s, telefono = %s WHERE ci = %s",
            (nombre, apellido, telefono, ci))
        cnx.commit()
        cnx.close()
        return "Tecnico modificado correctamente."

    except Exception as error:
        return "No se ha podido modificar el tecnico. Error al modificar el tecnico."
