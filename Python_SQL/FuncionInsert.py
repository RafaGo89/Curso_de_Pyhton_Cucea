import mysql.connector
import FuncionDeConexion

def interfazSql (id, title):
    try:
        conexion = FuncionDeConexion.conexionBd (1)
        cursor = conexion.cursor()
        sql = f"INSERT INTO materia (id, title) VALUES ('{id}', '{title}');"
        print (sql)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()
    
    except mysql.connector.Error as error:
        print ("Failed to update record to database rollback: {}".format(error))
        conexion.rollback()
        
    finally:
        print ("Conexión finalizada")
        conexion.close()
        cursor.close()
        
interfazSql('1003', 'Probabilidad')