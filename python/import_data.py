from pathlib import Path
from database.conexion import conectar
import pandas as pd, sqlite3 # type: ignore

BASE_DIR = Path(__file__).resolve().parent
ruta = BASE_DIR / "../data/raw"

def cargar_productos():
    """Carga los productos desde Excel."""
    return pd.read_excel(ruta / "productos.xlsx")

def cargar_clientes():
    """Carga los clientes desde Excel."""
    return pd.read_excel(ruta / "clientes.xlsx")

def cargar_ventas():
    """Carga las ventas desde Excel."""
    return pd.read_excel(ruta / "ventas.xlsx")

def importar_datos():
    """Carga los datos provenientes de Excel a la base de datos."""
    conexion = None
    try:
        conexion = conectar()
        print("Conexión establecida.")
    except sqlite3.Error as error:
        print(f'Falló la conexión a la base de datos: {error}')
    try:
        productos = cargar_productos()
        clientes = cargar_clientes()
        ventas = cargar_ventas()
        productos.to_sql("productos", conexion, if_exists="replace", index=False)
        clientes.to_sql("clientes", conexion, if_exists="replace", index=False)
        ventas.to_sql("ventas", conexion, if_exists="replace", index=False)
    except (FileNotFoundError, pd.errors.ParserError, ValueError) as error:
        print(f'Error al cargar los datos: {error}')
    else:
        print("Datos cargados correctamente.")
    finally:
        if conexion:
            conexion.close()
            print("Conexión cerrada.")
