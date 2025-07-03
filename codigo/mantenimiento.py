from base_de_datos import conexion
from datetime import datetime

def agregar_mantenimiento(id_maquina, ci_tecnico, tipo, fecha, observaciones):
    if not str(id_maquina).isdigit():
        return {"exito": False, "mensaje": "El id de la maquina debe ser numerico."}
    if not str(ci_tecnico).isdigit():
        return {"exito": False, "mensaje": "La cedula debe ser solo numeros, sin puntos, ni guiones."}
    if not tipo:
        return {"exito": False, "mensaje": "Tipo de mantenimiento no puede estar vacio."}
    try:
        datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")  # Validar formato de fecha
    except ValueError:
        return {"exito": False, "mensaje": "Fecha inválida. Formato esperado: YYYY-MM-DD HH:MM:SS"}

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        query = ("INSERT INTO mantenimientos (idMaquina, ciTecnico, tipo, fecha, observaciones) "
                 "VALUES (%s, %s, %s, %s, %s)") #%s para evitar injeccion y formatear correctamente los valores
        datos = (id_maquina, ci_tecnico, tipo, fecha, observaciones)
        cursor.execute(query, datos) #escribe la sentencia
        cnx.commit() #la ejecuta
        cnx.close() #cerramos la conexion
        return {"exito:": True, "mensaje": "Mantenimiento agregado correctamente."}
    except Exception as error:
        return {"exito": False, "mensaje": "Error al agregar el mantenimiento."}

def eliminar_mantenimiento(id):
    if not str(id).isdigit():
        return {"exito": False, "mensaje": "El id debe ser numerico."}

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM mantenimientos WHERE id = %s", (id,))
        mantenim = cursor.fetchone()

        if mantenim is None:
            return {"exito": False, "mensaje": "No existe ese mantenimiento con esa ID"}

        cursor.execute("DELETE FROM mantenimientos WHERE id = %s", (id,))
        cnx.commit()
        cnx.close()
        return {"exito:": True, "mensaje": "Mantenimiento eliminado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al eliminar el mantenimiento."}

def modificar_mantenimiento(id, id_maquina, ci_tecnico, tipo, fecha, observaciones):
    if not str(id).isdigit():
        return {"exito": False, "mensaje": "El id debe ser numerico."}
    if not str(id_maquina).isdigit():
        return {"exito": False, "mensaje": "El id de la maquina debe ser numerico."}
    if not str(ci_tecnico).isdigit():
        return {"exito": False, "mensaje": "La cedula debe ser solo numeros, sin puntos, ni guiones."}
    if not tipo:
        return {"exito": False, "mensaje": "Tipo de mantenimiento no puede estar vacio."}
    try:
        datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")  # Validar formato de fecha
    except ValueError:
        return {"exito": False, "mensaje": "Fecha inválida. Formato esperado: YYYY-MM-DD HH:MM:SS"}

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM mantenimientos WHERE id = %s", (id,))
        mantenim = cursor.fetchone()

        if mantenim is None:
            return {"exito": False, "mensaje": "No existe ese mantenimiento con esa ID"}

        query = ("UPDATE mantenimientos SET idMaquina = %s, ciTecnico = %s, tipo = %s, fecha = %s, observaciones = %s "
                 "WHERE id = %s")
        cursor.execute(query, (id_maquina, ci_tecnico, tipo, fecha, observaciones, id))
        cnx.commit()
        cnx.close()
        return {"exito:": True, "mensaje": "Mantenimiento modificado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al modificar el mantenimiento."}