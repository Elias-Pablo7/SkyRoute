import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="username",           # ← Cambiá esto si tu usuario MySQL es otro
        password="********", # ← Cambiá por tu contraseña real
        database="skyroute"
    )
