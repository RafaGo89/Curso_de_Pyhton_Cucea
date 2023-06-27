import mysql.connector
import FuncionDeConexion

def interfazSql (sql, columnas, tablas, parametros):
    try:
        conexion = FuncionDeConexion.conexionBd (1)
        cursor = conexion.cursor()
        cursor.execute(sql, [columnas, tablas, parametros])
        registros = cursor.fetchall()
        
        for elemento in registros:
            print (elemento)
    
    except mysql.connector.Error as error:
        print ("Ocurrió un error al conectar: ", error)
    
    finally:
        print ("Conexión finalizada")
        conexion.close()
        
interfazSql ("Select %s from %s where name like '%s%'", 'name, lastname', 'maestro', 'd')