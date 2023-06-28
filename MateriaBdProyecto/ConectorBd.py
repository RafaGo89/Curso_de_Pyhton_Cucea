import mysql.connector

selectorBaseDeDatos = "local"

def conexion (selectorBaseDeDatos):
    if selectorBaseDeDatos == "local":
        #Base de datos local
        host = "127.0.0.1"
        user = "root"
        password = ""
        port = 3306
        database = "mini-siiau"
    
    elif selectorBaseDeDatos == "remoto":
        #Base de datos remota
        host = "142.44.163.242"
        user = "Alumno9"
        password = "AlumnoPython1@."
        port = 4000
        database = "mini-siiau"
    
    conexion = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        port = port,
        database = database
    )
    
    return conexion