import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # ← Cambiá esto si tu usuario MySQL es otro
        password="Uuusdvt3", # ← Cambiá por tu contraseña real
        database="skyroute"
    )