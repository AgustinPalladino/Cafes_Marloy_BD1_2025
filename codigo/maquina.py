from base_de_datos import conexion

def agregar_maquina(modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual, usuario):
    if not modelo or not ubicacion_cliente:
        return "No se ha podido agregar la maquina. Modelo y ubicación no pueden estar vacios."
    if not str(id_cliente).isdigit():
        return "No se ha podido agregar la maquina. El id del cliente debe ser numerico."
    if not costo_alquiler_mensual > 0:
        return "No se ha podido agregar la maquina. El costo debe ser un numero positivo."

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO maquinas (modelo, idCliente, ubicacionCliente, costoAlquilerMensual) VALUES (%s, %s, %s, %s)",
                       (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual))
        cnx.commit()
        cursor.close()
        cnx.close()
        return "Maquina agregada correctamente."

    except Exception as error:
        return "No se ha podido agregar la maquina. Error al agregar la maquina."

def eliminar_maquina(id, usuario):
    if not str(id).isdigit():
        return "No se ha podido eliminar la maquina. El id debe ser numerico."

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM maquinas WHERE id = %s", (id,))
        maquin = cursor.fetchone()
        if maquin is None:
            return "No se ha podido eliminar la maquina. No existe maquina con esa ID"
        
        cursor.execute("SELECT COUNT(*) FROM mantenimientos WHERE idMaquina = %s", (id,))
        if cursor.fetchone()[0] > 0:
            return "No se ha podido eliminar la maquina. La máquina tiene mantenimientos asignados y no puede ser eliminada."

        cursor.execute("DELETE FROM maquinas WHERE id = %s", (id,))
        cnx.commit()
        cnx.close()
        return "Maquina eliminada correctamente."

    except Exception as error:
        return "No se ha podido eliminar la maquina. Error al eliminar la maquina."

def modificar_maquina(id, modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual, usuario):
    if not str(id).isdigit():
        return "No se ha podido modificar la maquina. El id debe ser numerico."
    if not modelo or not ubicacion_cliente:
        return "No se ha podido modificar la maquina. Modelo y ubicación no pueden estar vacios."
    if not str(id_cliente).isdigit():
        return "No se ha podido modificar la maquina. El id del cliente debe ser numerico."
    if not costo_alquiler_mensual > 0:
        return "No se ha podido modificar la maquina. El costo debe ser un numero positivo."

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM maquinas WHERE id = %s", (id,))
        maquin = cursor.fetchone()
        if maquin is None:
            return "No se ha podido modificar la maquina. No existe maquina con esa ID"

        cursor.execute("UPDATE maquinas SET modelo = %s, idCliente = %s, ubicacionCliente = %s, "
                       "costoAlquilerMensual = %s WHERE id = %s",
                       (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual, id))
        cnx.commit()
        cnx.close()
        return "Maquina modificada correctamente."

    except Exception as error:
        return "No se ha podido modificar la maquina. Error al modificar la maquina."