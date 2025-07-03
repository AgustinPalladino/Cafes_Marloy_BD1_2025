from base_de_datos import conexion
from datetime import datetime

def agregar_consumo(id_maquina, id_insumo, cantidad_usada, fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")  # Validar formato de fecha
    except ValueError:
        return {"exito": False, "mensaje": "Fecha inválida. Formato esperado: YYYY-MM-DD"}

    try:
        cnx = conexion()
        cursor = cnx.cursor() #traemos la conexion de la clase base_de_datos
        query = "INSERT INTO registroConsumo (idMaquina, idInsumo, fecha, cantidadUsada) VALUES (%s, %s, %s, %s)" #%s para evitar injeccion y formatear correctamente los valores
        datos = (id_maquina, id_insumo, cantidad_usada, fecha)
        cursor.execute(query, datos) #junta la sentencia
        cnx.commit() #la ejecuta
        cnx.close()
        return {"exito:": True, "mensaje": "Registro consumo agregado correctamente."}

    except Exception as error:
        return {"exito": False, "mensaje": "Error al registrar consumo."}

def calcular_costo_insumos_mensual(mes, anio):
    try:
        cnx = conexion()
        cursor = cnx.cursor() #traemos la conexion de la clase base_de_datos
        query = ("SELECT c.nombre AS cliente, "
                "SUM(rc.cantidadUsada * i.precioUnitario) AS costo_total_insumos "
                "FROM registroConsumo rc "
                "JOIN maquinas m ON rc.idMaquina = m.id "
                "JOIN clientes c ON m.idCliente = c.id "
                "JOIN insumos i ON rc.idInsumo = i.id "
                "WHERE MONTH(rc.fecha) = %s AND YEAR(rc.fecha) = %s "
                "GROUP BY c.nombre "
                "ORDER BY costo_total_insumos DESC") #%s para evitar injeccion y formatear correctamente los valores

        cursor.execute(query, (mes, anio)) #junta la sentencia
        resultados = cursor.fetchall()

        cnx.commit() #la ejecuta
        cnx.close()

        lista_resultado = []
        for cliente, costo in resultados:
            lista_resultado.append({
                "cliente": cliente,
                "costo_total": round(costo, 2)
            })

        return {"exito": True, "mensaje": lista_resultado}

    except Exception as error:
      return {"exito": False, "mensaje": "Error al calcular el costo mensual."}
