from base_de_datos import conexion

def agregar_maquina(modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual, usuario):
    if not usuario[1]:
        return {"exito": False, "mensaje": "Permiso rechazado, necesita ser administrador."}
    if not modelo or not ubicacion_cliente:
        return {"exito": False, "mensaje": "Modelo y ubicación no pueden estar vacios."}
    if not str(id_cliente).isdigit():
        return {"exito": False, "mensaje": "El id del cliente debe ser numerico."}
    if not costo_alquiler_mensual > 0:
        return {"exito": False, "mensaje": "El costo debe ser un numero positivo."}

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("insert into maquinas (modelo, idCliente, ubicacionCliente, costoAlquilerMensual) values (%s, %s, %s, %s)",
                       (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual))
        cnx.commit()
        cursor.close()
        cnx.close()
        return {"exito:": True, "mensaje": "Maquina agregada correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al agregar la maquina."}

def eliminar_maquina(id, usuario):
    if not usuario[1]:
        return {"exito": False, "mensaje": "Permiso rechazado, necesita ser administrador."}
    if not str(id).isdigit():
        return {"exito": False, "mensaje": "El id debe ser numerico."}

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("select * from maquinas where id = %s", (id,))
        maquin = cursor.fetchone()
        if maquin is None:
            return {"exito": False, "mensaje": "No existe maquina con esa ID"}
        
        cursor.execute("SELECT COUNT(*) FROM mantenimientos WHERE idMaquina = %s", (id,))
        if cursor.fetchone()[0] > 0:
            return {"exito": False, "mensaje": "La máquina tiene mantenimientos asignados y no puede ser eliminada."}


        cursor.execute("delete from maquinas where id = %s", (id,))
        cnx.commit()
        cnx.close()
        return {"exito:": True, "mensaje": "Maquina eliminada correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al eliminar la maquina."}

def modificar_maquina(id, modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual, usuario):
    if not usuario[1]:
        return {"exito": False, "mensaje": "Permiso rechazado, necesita ser administrador."}
    if not str(id).isdigit():
        return {"exito": False, "mensaje": "El id debe ser numerico."}
    if not modelo or not ubicacion_cliente:
        return {"exito": False, "mensaje": "Modelo y ubicación no pueden estar vacios."}
    if not str(id_cliente).isdigit():
        return {"exito": False, "mensaje": "El id del cliente debe ser numerico."}
    if not costo_alquiler_mensual > 0:
        return {"exito": False, "mensaje": "El costo debe ser un numero positivo."}

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("select * from maquinas where id = %s", (id,))
        maquin = cursor.fetchone()
        if maquin is None:
            return {"exito": False, "mensaje": "No existe maquina con esa ID"}

        cursor.execute("UPDATE maquinas SET modelo = %s, idCliente = %s, ubicacionCliente = %s, "
                       "costoAlquilerMensual = %s WHERE id = %s",
                       (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual, id))
        cnx.commit()
        cnx.close()
        return {"exito:": True, "mensaje": "Maquina modificada correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al modificar la maquina."}