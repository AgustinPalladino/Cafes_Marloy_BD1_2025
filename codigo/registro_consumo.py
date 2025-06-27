from base_de_datos import conexion

def agregar_consumo(id_maquina, id_insumo, cantidad_usada, fecha):
    try:
        cnx = conexion()
        cursor = cnx.cursor() #traemos la conexion de la clase base_de_datos
        query = "INSERT INTO registroConsumo (idMaquina, idInsumo, fecha, cantidadUsada) VALUES (%s, %s, %s, %s)" #%s para evitar injeccion y formatear correctamente los valores
        datos = (id_maquina, id_insumo, cantidad_usada, fecha)
        cursor.execute(query, datos) #junta la sentencia
        cnx.commit() #la ejecuta
        cnx.close()
        return

    except Exception as error:
        return

def calcular_costo_insumos_mensual(mes, anio):
    try:
        cnx = conexion()
        cursor = cnx.cursor() #traemos la conexion de la clase base_de_datos
        query = ("SELECT c.nombre AS cliente, SUM(rc.cantidadUsada * i.precioUnitario) AS costo_total_insumos"
                 "from registroConsumo rc"
                 "join maquinas m ON rc.idMaquina = m.id"
                 "join clientes c ON m.idCliente = c.id"
                 "join insumos i ON rc.idInsumos = i.id"
                 "where MONTH(rc.fecha) = %s AND YEAR(rc.fecha) = %s"
                 "group by c.nombre"
                 "order by costo_total_insumos DESC") #%s para evitar injeccion y formatear correctamente los valores

        cursor.execute(query, (mes, anio)) #junta la sentencia
        resultados = cursor.fetchall()

        cnx.commit() #la ejecuta
        cnx.close()

        lista_resultado = [] #devolvemos un diccionario para los que se encargan del front end, cosas a cambiar: las demas funciones
        for cliente, costo in resultados:
            lista_resultado.append({
                "cliente": cliente,
                "costo_total": round(costo, 2)
            })

        return lista_resultado

    except Exception as error:
        return