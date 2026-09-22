import pandas as pd # type: ignore
from .conexion import *

def consultar(consulta):
    """Ejecuta consultas a la base de datos."""
    conexion = None
    try:
        # intentar conectar a la base de datos, consultar y obtener los resultados de la consulta en un DataFrame
        conexion = conectar()
        df = pd.read_sql_query(consulta, conexion)
    except pd.errors.DatabaseError as error:
        # si falla la conexión, mostrar un mensaje de error
        print(f'Falló la conexión a la base de datos: {error}')
    else:
        # si la conexión es exitosa, devolver el DataFrame
        print("Conexión exitosa.")
        return df
    finally:
        # si hubo conexión, cerrarla
        if conexion:
            conexion.close()
            print("Conexión cerrada.")

def obtener_productos():
    """Obtiene productos de la base de datos."""
    return consultar("SELECT * FROM productos;")

def obtener_clientes():
    """Obtiene clientes de la base de datos."""
    return consultar("SELECT * FROM clientes;")

def obtener_ventas():
    """Obtiene ventas de la base de datos."""
    return consultar("SELECT * FROM ventas;")
