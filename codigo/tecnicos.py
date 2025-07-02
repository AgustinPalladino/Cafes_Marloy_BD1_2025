from base_de_datos import conexion

def agregar_tecnico(ci, nombre, apellido, telefono, usuario):
    if not usuario[1]: # si no es admin no puede agregar
        return {"exito": False, "mensaje": "Permiso rechazado, necesita ser administrador."}
    if not str(ci).isdigit():
        return {"exito": False, "mensaje": "La cedula debe ser solo numeros, sin puntos, ni guiones."}
    if not telefono or not str(telefono).isdigit():
        return {"exito": False, "mensaje": "El telefono debe contener solo numeros."}
    if not nombre or not apellido:
        return {"exito": False, "mensaje": "Nombre y apellidos vacios"}

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("insert into tecnicos (ci, nombre, apellido, telefono) values (%s, %s, %s, %s)",
                       (ci,nombre, apellido, telefono))
        cnx.commit()
        cursor.close()
        cnx.close()
        return {"exito:": True, "mensaje": "Tecnico agregado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al agregar el tecnico."}


def eliminar_tecnico(ci, usuario):
    if not usuario[1]:
        return {"exito": False, "mensaje": "Permiso rechazado, necesita ser administrador."}
    if not str(ci).isdigit():
        return {"exito": False, "mensaje": "La cedula debe ser solo numeros, sin puntos, ni guiones."}

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("select * from tecnicos where ci = %s", (ci,))
        tec = cursor.fetchone()
        if tec is None:
            return {"exito": False, "mensaje": "No existe ese tecnico con esa cedula"}

        cursor.execute("delete from tecnicos where ci = %s", (ci,))
        cnx.commit()
        cnx.close()
        return {"exito:": True, "mensaje": "Tecnico eliminado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al eliminar el tecnico."}

def modificar_tecnico(ci, nombre, apellido, telefono, usuario):
    if not usuario[1]:
        return {"exito": False, "mensaje": "Permiso rechazado, necesita ser administrador."}
    if not str(ci).isdigit():
        return {"exito": False, "mensaje": "La cedula debe ser solo numeros, sin puntos, ni guiones."}
    if not telefono or not str(telefono).isdigit():
        return {"exito": False, "mensaje": "El telefono debe contener solo numeros."}
    if not nombre or not apellido:
        return {"exito": False, "mensaje": "Nombre y apellidos vacios"}

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("select * from tecnicos where ci = %s", (ci,))
        tec = cursor.fetchone()
        if tec is None:
            return {"exito": False, "mensaje": "No existe ese tecnico con esa cedula"}

        cursor.execute("UPDATE tecnicos SET nombre = %s, apellido = %s, telefono = %s WHERE ci = %s",
            (nombre, apellido, telefono, ci))
        cnx.commit()
        cnx.close()
        return {"exito:": True, "mensaje": "Tecnico modificado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al modificar el tecnico."}
