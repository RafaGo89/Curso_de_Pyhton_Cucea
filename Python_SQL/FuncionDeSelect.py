import mysql.connector
import FuncionDeConexion

def interfazSql (columna, tabla, parametro):
    try:
        conexion = FuncionDeConexion.conexionBd (1)
        cursor = conexion.cursor()
        sql = f"SELECT {columna} from {tabla} where name like '{parametro}%';"
        cursor.execute(sql)
        registros = cursor.fetchall()
        
        for elemento in registros:
            print (elemento)
    
    except mysql.connector.Error as error:
        print ("Ocurrió un error al conectar: ", error)
    
    finally:
        print ("Conexión finalizada")
        conexion.close()
        cursor.close()
        
interfazSql('name, lastname', 'maestro', 'a')