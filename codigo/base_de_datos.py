import mysql.connector

def conexion():
    return mysql.connector.connect(host='127.0.0.1', user='root', password='rootpassword', database= 'cafesmarloy')
