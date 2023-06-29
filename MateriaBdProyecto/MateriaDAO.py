#CRUD
import mysql.connector
import ConectorBd
import Materia

def altaMateria(id, title):
    try:
        conexion = ConectorBd.conexion("local")
        cursor = conexion.cursor()
        sql = f"INSERT INTO materia (id, title) VALUES ('{id}', '{title}');"
        cursor.execute(sql)
        print (sql)
        conexion.commit()
    
    except mysql.connector.Error as error:
        print ("Ocurrió un error al conectar: ", error)
    
    finally:
        conexion.close()
        cursor.close()

def verMateria(id):
    try:
        conexion = ConectorBd.conexion("local")
        cursor = conexion.cursor()
        sql = f"SELECT id, title from materia where id = {id}"
        cursor.execute(sql)
        registros = cursor.fetchall()
        
        for elemento in registros:
            #materia = Materia(elemento[0], elemento[1])
            print (f"id = {elemento[0]} Nombre = {elemento[1]}")
    
    except mysql.connector.Error as error:
        print ("Ocurrió un error al conectar: ", error)
    
    finally:
        conexion.close()
        cursor.close()

def verTodasMateria():
    try:
        conexion = ConectorBd.conexion("local")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM materia")
        registros = cursor.fetchall()
        
        for elemento in registros:
            #materia = Materia(elemento[0], elemento[1])
            print (f"id = {elemento[0]} Nombre = {elemento[1]}")
    
    except mysql.connector.Error as error:
        print ("Ocurrió un error al conectar: ", error)
    
    finally:
        conexion.close()
        cursor.close()

def modificarMateria(id, title):
    try:
        conexion = ConectorBd.conexion("local")
        cursor = conexion.cursor()
        sql = f"UPDATE materia SET title = '{title}' WHERE id = {id};"
        cursor.execute(sql)
        print (sql)
        conexion.commit()
    
    except mysql.connector.Error as error:
        print ("Ocurrió un error al conectar: ", error)
    
    finally:
        conexion.close()
        cursor.close()

def eliminarMateria(id):
    try:
        conexion = ConectorBd.conexion("local")
        cursor = conexion.cursor()
        sql = f"DELETE from materia where id = {id};"
        cursor.execute(sql)
        print (sql)
        conexion.commit()
    
    except mysql.connector.Error as error:
        print ("Ocurrió un error al conectar: ", error)
    
    finally:
        conexion.close()
        cursor.close()
