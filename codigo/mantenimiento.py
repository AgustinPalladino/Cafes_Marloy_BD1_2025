from base_de_datos import conexion
from datetime import datetime

def agregar_mantenimiento(id_maquina, ci_tecnico, tipo, fecha, observaciones):
    if not str(id_maquina).isdigit():
        return "No se ha podido agregar el mantenimiento. El id de la maquina debe ser numerico."
    if not str(ci_tecnico).isdigit():
        return "No se ha podido agregar el mantenimiento. La cedula debe ser solo numeros, sin puntos, ni guiones."
    if not tipo:
        return "No se ha podido agregar el mantenimiento. Tipo de mantenimiento no puede estar vacio."
    try:
        datetime.strptime(fecha, "%Y-%M-%D %H:%M:%S")  # Validar formato de fecha
    except ValueError:
        return "No se ha podido agregar el mantenimiento. Fecha inválida. Formato esperado: YYYY-MM-DD HH:MM:SS"

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        query = ("INSERT INTO mantenimientos (idMaquina, ciTecnico, tipo, fecha, observaciones) "
                 "VALUES (%s, %s, %s, %s, %s)") #%s para evitar injeccion y formatear correctamente los valores
        datos = (id_maquina, ci_tecnico, tipo, fecha, observaciones)
        cursor.execute(query, datos) #escribe la sentencia
        cnx.commit() #la ejecuta
        cnx.close() #cerramos la conexion
        return "Mantenimiento agregado correctamente."
    except Exception as error:
        return "No se ha podido agregar el mantenimiento. Error al agregar el mantenimiento."

def eliminar_mantenimiento(id):
    if not str(id).isdigit():
        return "No se ha podido eliminar el mantenimiento. El id debe ser numerico."

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM mantenimientos WHERE id = %s", (id,))
        mantenim = cursor.fetchone()

        if mantenim is None:
            return "No se ha podido eliminar el mantenimiento. No existe ese mantenimiento con esa ID"

        cursor.execute("DELETE FROM mantenimientos WHERE id = %s", (id,))
        cnx.commit()
        cnx.close()
        return "Mantenimiento eliminado correctamente."

    except Exception as error:
        return "No se ha podido eliminar el mantenimiento. Error al eliminar el mantenimiento."

def modificar_mantenimiento(id, id_maquina, ci_tecnico, tipo, fecha, observaciones):
    if not str(id).isdigit():
        return "No se ha podido modificar el mantenimiento. El id debe ser numerico."
    if not str(id_maquina).isdigit():
        return "No se ha podido modificar el mantenimiento. El id de la maquina debe ser numerico."
    if not str(ci_tecnico).isdigit():
        return "No se ha podido modificar el mantenimiento. La cedula debe ser solo numeros, sin puntos, ni guiones."
    if not tipo:
        return "No se ha podido modificar el mantenimiento. Tipo de mantenimiento no puede estar vacio."
    try:
        datetime.strptime(fecha, "%Y-%M-%D %H:%M:%S")  # Validar formato de fecha
    except ValueError:
        return "No se ha podido modificar el mantenimiento. Fecha inválida. Formato esperado: YYYY-MM-DD HH:MM:SS"

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM mantenimientos WHERE id = %s", (id,))
        mantenim = cursor.fetchone()

        if mantenim is None:
            return "No se ha podido modificar el mantenimiento. No existe ese mantenimiento con esa ID"

        query = ("UPDATE mantenimientos SET idMaquina = %s, ciTecnico = %s, tipo = %s, fecha = %s, observaciones = %s "
                 "WHERE id = %s")
        cursor.execute(query, (id_maquina, ci_tecnico, tipo, fecha, observaciones, id))
        cnx.commit()
        cnx.close()
        return "Mantenimiento modificado correctamente."

    except Exception as error:
        return "No se ha podido modificar el mantenimiento. Error al modificar el mantenimiento."