#CRUD
import mysql.connector
import ConectorBd
import Materia

def altaMateria():
    pass

def verMateria():
    pass

def verTodasMateria():
    try:
        conexion = ConectorBd.conexion("local")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM materia")
        registros = cursor.fetchall()
        
        for elemento in registros:
            #materia = Materia(elemento[0], elemento[1])
            print (f"id = {elemento[0]} título = {elemento[1]}")
    
    except mysql.connector.Error as error:
        print ("Ocurrió un error al conectar: ", error)
    
    finally:
        print ("Conexión finalizada")
        conexion.close()
        cursor.close()

def modificarMateria():
    pass

def eliminarMateria():
    pass
