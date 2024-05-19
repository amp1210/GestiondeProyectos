import os
import pathlib
import sqlite3

class ConexionSQLite:
    
    def __init__ (self):
        self.nombre_archivo = 'basedatos.bd'
        absolutepath = os.path.abspath(__file__)
        parentdirectory = os.path.dirname(absolutepath)
        self.ruta_base_de_datos = pathlib.Path(parentdirectory)
        self.conexion = None
        
    def conectar(self):
        try:
            self.conexion = sqlite3.connect(f"{self.ruta_base_de_datos}\{self.nombre_archivo}")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
    
    def desconectar(self):
        try:
            if self.conexion:
                self.conexion.close()
        except Exception as e:
            print(f"Error al cerrar la conexión: {e}")
    
    def ejecutar_query(self, query, valores):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, valores)
            self.conexion.commit()
            return True
        except Exception as e:
            print(f"Error al ejecutar el query: {e}")
            return False
    
    def fetch_all_data(self, query, valores=None):
        try:
            #se inicializa el cursor para apuntar a la base de datos y enviar la consulta.
            cursor = self.conexion.cursor()
            #se evalua si la consulta viene con valores para filtro, si los trae, se enviara el query
            #mas los valores.
            if valores:
                cursor.execute(query, valores)
            #Si no viene la variable de los valores, se enviara el query solo
            else:
                cursor.execute(query)
            #se realiza la consulta para que devuelva todo lo que existe en la base de datos.
            data = cursor.fetchall()
            #se retorna la informacion que devuelve la base de datos.
            return data
        except Exception as e:
            print(f"Error al obtener los datos: {e}")

    def fetch_one_data(self, query, valores):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(query, valores)
            data = cursor.fetchone()
            return data
        except Exception as e:
            print(f"Error al obtener los datos: {e}")