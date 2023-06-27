import mysql.connector

opcionBaseDeDatos = 1

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

try:
    conexion = mysql.connector.connect(
        host = host,
        user = user,
        passwd = passwd,
        port = port,
        database = database
    )
    
    cursor = conexion.cursor()
    cursor.execute ("Show tables")
    registros = cursor.fetchall()
        
    for elemento in registros:
        print (elemento)
        
    cursor.execute ("Select name, lastname from Maestro")
    registros = cursor.fetchall()
    
    for elemento in registros:
        print (elemento)
    
except mysql.connector.Error as error:
    print ("Ocurrió un error al conectar: ", error)
    
finally:
    print ("Conexión finalizada")
    conexion.close()