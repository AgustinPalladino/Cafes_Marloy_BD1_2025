import mysql.connector

def conexion():
    return mysql.connector.connect(host='127.0.0.1', user='root', password='07102005Sebastian', database= 'CafesMarloy')

def login(correo, contraseña):
    cnx = conexion()
    cursor = cnx.cursor()

    cursor.execute("SELECT correo, esAdministrador FROM login WHERE correo = %s AND contraseña = %s", (correo, contraseña))
    user = cursor.fetchone()

    cnx.close()

    if user:
        return user
    else:
        return None 