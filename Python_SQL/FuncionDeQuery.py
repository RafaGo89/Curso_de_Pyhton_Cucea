import mysql.connector
import FuncionDeConexion

def interfazSql (sql):
    try:
        conexion = FuncionDeConexion.conexionBd (1)
        cursor = conexion.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        
        for elemento in registros:
            print (elemento)
    
    except mysql.connector.Error as error:
        print ("Ocurrió un error al conectar: ", error)
    
    finally:
        print ("Conexión finalizada")
        conexion.close()
        
interfazSql("Select title from materia where title like 'e%'")