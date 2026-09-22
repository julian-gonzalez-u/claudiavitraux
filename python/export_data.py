from pathlib import Path
from dataclasses import asdict
import pandas as pd # type: ignore
from python.models import *
from python.utils import *

BASE_DIR = Path(__file__).resolve().parent
ruta = BASE_DIR / "../data/raw"

def crear_producto():
    """Agrega un producto a Excel."""
    try:
        # pedir los datos del producto
        id = int(input("Ingrese el ID numérico: \n"))
        nombre = input("Ingrese el nombre del producto: \n")
        categoria = input("Ingrese a qué categoría pertenece el producto: \n")
        precio = float(input("Ingrese el precio del producto: \n"))
        stock = int(input("Ingrese el stock del producto: \n"))
    except (TypeError, ValueError):
        print("Datos no válidos.")
        return None
    producto = Producto(id, nombre, categoria, precio, stock)
    datos = asdict(producto)
    datos["categoría"] = datos.pop("categoria")
    df_nuevo = pd.DataFrame([datos])
    df_productos = pd.read_excel(ruta / "productos.xlsx")
    df_productos = pd.concat([df_productos, df_nuevo], ignore_index=True)
    try:
        df_productos.to_excel(ruta / "productos.xlsx", index=False)
    except PermissionError:
        print("No se pudo modificar el archivo. Comprueba que Excel esté cerrado.")

def crear_clientes():
    """Agrega clientes a Excel."""
    cantidad = int(input("Ingrese la cantidad de clientes a registrar: \n"))
    ultimo_id = pd.read_excel(ruta / "clientes.xlsx")["id_cliente"].max()
    clientes = []
    for id_cliente in range(ultimo_id + 1, ultimo_id + cantidad + 1):
        try:
            # pedir los datos de cada cliente
            nombre = input(f'Nombre del cliente {id_cliente}: \n')
            telefono = int(input(f'Número de teléfono del cliente {id_cliente}: \n'))
        except (TypeError, ValueError):
            print("Datos no válidos.")
            return None
        cliente = Cliente(id_cliente, nombre, telefono)
        clientes.append(cliente)
    for i in range(len(clientes)):
        datos = asdict(clientes[i])
        datos["teléfono"] = datos.pop("telefono")
        df_nuevo = pd.DataFrame([datos])
        df_clientes = pd.read_excel(ruta / "clientes.xlsx")
        df_clientes = pd.concat([df_clientes, df_nuevo], ignore_index=True)
        try:
            df_clientes.to_excel(ruta / "clientes.xlsx", index=False)
        except PermissionError:
            print("No se pudo modificar el archivo. Comprueba que Excel esté cerrado.")

def registrar_venta():
    """Registra una venta en Excel."""
    ultimo_id = pd.read_excel(ruta / "ventas.xlsx")["id_venta"].max()
    try:
        # pedir los datos de la venta
        fecha = input("Ingrese la fecha de la venta en formato dd/mm/YYYY: \n")
        fecha = formatear_fecha(fecha)
        id_cliente = int(input("Ingrese el ID del cliente que hizo la compra: \n"))
        id_producto = int(input("Ingrese el ID del producto vendido: \n"))
        cantidad = int(input("Ingrese la cantidad de unidades vendidas: \n"))
        precio = float(input("Ingrese el precio por unidad: \n"))
    except (TypeError, ValueError):
        print("Datos no válidos.")
        return None
    venta = Venta(ultimo_id + 1, fecha, id_cliente, id_producto, cantidad, precio)
    datos = asdict(venta)
    df_nuevo = pd.DataFrame([datos])
    df_ventas = pd.read_excel(ruta / "ventas.xlsx")
    df_ventas = pd.concat([df_ventas, df_nuevo], ignore_index=True)
    try:
        df_ventas.to_excel(ruta / "ventas.xlsx", index=False)
    except PermissionError:
        print("No se pudo modificar el archivo. Comprueba que Excel esté cerrado.")
