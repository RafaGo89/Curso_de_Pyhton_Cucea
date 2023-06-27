import mysql.connector

def conexionBd (opcionBaseDeDatos):
    if opcionBaseDeDatos == 1 :
        #manera local
        host = "127.0.0.1"
        user = "root"
        passwd = ""
        port = 3306
        database = "mini-siiau"

    elif opcionBaseDeDatos == 2 :
        #manera en línea
        host = "142.44.163.242"
        user = "Alumno9"
        passwd = "AlumnoPython1@."
        port = 4000
        database = "mini-siiau"
    
    conexion = mysql.connector.connect(
        host = host,
        user = user,
        passwd = passwd,
        port = port,
        database = database
    )
    
    return conexion
