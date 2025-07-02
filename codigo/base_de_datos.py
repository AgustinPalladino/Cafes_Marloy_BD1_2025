import mysql.connector

def conexion():
    return mysql.connector.connect(host='127.0.0.1', user='root', password='rootpassword', database= 'cafesmarloy')

def login(correo, contraseña):
    cnx = conexion()
    cursor = cnx.cursor()

    cursor.execute("select correo, esAdministrador from login where correo = %s and contraseña = %s", (correo, contraseña))
    user = cursor.fetchone()

    cnx.close()

    if user:
        return user
    else:
        return None #Usar string?