from base_de_datos import conexion

def agregar_maquina(modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual, usuario):
    if not usuario[1]: # si no es admin no puede agregar proveedores
        return

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("insert into maquinas (modelo, idCliente, ubicacionCliente, costoAlquilerMensual) values (%s, %s, %s, %s)",
                       (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual))
        cnx.commit()
        cursor.close()
        cnx.close()
        return

    except Exception as error:
        return

def eliminar_maquina(id, usuario):
    if not usuario[1]:
        return

    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("select * from maquinas where id = %s", (id,))
        maquin = cursor.fetchone()
        if maquin is None:
            return

        cursor.execute("delete from maquinas where id = %s", (id,))
        cnx.commit()
        cnx.close()
        return

    except Exception as error:
        return

def modificar_maquina(id, modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual, usuario):
    if not usuario[1]:
        return

    try:
        cnx = conexion()
        cursor = cnx.cursor()
        cursor.execute("select * from maquinas where id = %s", (id,))
        maquin = cursor.fetchone()
        if maquin is None:
            return

        cursor.execute("UPDATE maquinas SET modelo = %s, idCliente = %s, ubicacionCliente = %s, "
                       "costoAlquilerMensual = %s WHERE id = %s",
                       (modelo, id_cliente, ubicacion_cliente, costo_alquiler_mensual, id))
        cnx.commit()
        cnx.close()
        return

    except Exception as error:
        return