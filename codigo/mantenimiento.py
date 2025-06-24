from base_de_datos import conexion

def agregar_mantenimiento(id_maquina, ci_tecnico, tipo, fecha, observaciones):
    try:
        cnx = conexion()
        cursor = cnx.cursor()
        query = ("INSERT INTO mantenimientos (idMaquina, ciTecnico, tipo, fecha, observaciones) "
                 "VALUES (%s, %s, %s, %s, %s)") #%s para evitar injeccion y formatear correctamente los valores
        datos = (id_maquina, ci_tecnico, tipo, fecha, observaciones)
        cursor.execute(query, datos) #escribe la sentencia
        cnx.commit() #la ejecuta
        cnx.close() #cerramos la conexion
        return #evaluar si tiene que retornar un string o un booleano

    except Exception as error:
        return

def eliminar_mantenimiento(id):
    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM mantenimientos WHERE id = %s", (id,))
        mantenim = cursor.fetchone()

        if mantenim is None:
            return

        cursor.execute("DELETE FROM mantenimientos WHERE id = %s", (id,))
        cnx.commit()
        cnx.close()
        return
    except Exception as error:
        return

def modificar_mantenimiento(id, id_maquina, ci_tecnico, tipo, fecha, observaciones):
    try:
        cnx = conexion()
        cursor = cnx.cursor()

        cursor.execute("SELECT * FROM mantenimientos WHERE id = %s", (id,))
        clnte = cursor.fetchone()

        if clnte is None:
            return

        query = ("UPDATE mantenimientos SET idMaquina = %s, ciTecnico = %s, tipo = %s, fecha = %s, observaciones = %s "
                 "WHERE id = %s")
        cursor.execute(query, (id_maquina, ci_tecnico, tipo, fecha, observaciones, id))
        cnx.commit()
        cnx.close()
        return
    except Exception as error:
        return