from base_de_datos import conexion

cnx = conexion()
cursor = cnx.cursor() #traemos la conexion de la clase base_de_datos

def agregar_insumo(descripcion, tipo, precioUnitario, id_proveedor):
    query = "INSERT INTO insumos (descripcion, tipo, precioUnitario, id_proveedor) VALUES (%s, %s, %s, %s)" #%s para evitar injeccion y formatear correctamente los valores
    datos = (descripcion, tipo, precioUnitario, id_proveedor)
    cursor.execute(query, datos) #junta la sentencia
    cnx.commit() #la ejecuta


def eliminar_insumo(id):
    try:
        cursor.execute("SELECT * FROM insumos WHERE id = %s", (id,))
        cliente = cursor.fetchone()

        if cliente is None:
            return

        cursor.execute("DELETE FROM insumos WHERE id = %s", (id,))
        cnx.commit()
    except Exception as e:
        return


def modificar_insumo(id, descripcion, tipo, precioUnitario, id_proveedor):
    try:
        query = "UPDATE insumos SET descripcion = %s, tipo = %s, precioUnitario = %s, id_proveedor = %s WHERE id = %s"

        cursor.execute(query, (descripcion, tipo, precioUnitario, id_proveedor, id))
        cnx.commit()
        return

    except Exception as e:
        return