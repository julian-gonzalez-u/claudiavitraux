import pandas as pd # type: ignore
from python.algoritmos.sorting import bubble_sort, selection_sort, insertion_sort, mergesort, quicksort

def calcular_ventas_totales(ventas):
    """Calcula las ventas totales."""
    importe = ventas["cantidad"] * ventas["precio"]
    return importe.sum()

def calcular_promedio_venta(ventas):
    """Calcula el promedio por cada venta."""
    total = calcular_ventas_totales(ventas)
    cantidad = ventas["cantidad"].sum()
    return total / cantidad

def producto_mas_vendido(ventas):
    """Devuelve el ID del producto más vendido."""
    return ventas.groupby("id_producto")["cantidad"].sum().idxmax()
    
def producto_menos_vendido(ventas):
    """Devuelve el ID del producto menos vendido."""
    return ventas.groupby("id_producto")["cantidad"].sum().idxmin()

def ventas_por_mes(ventas):
    """Calcula las ventas totales por mes."""
    ventas["fecha"] = pd.to_datetime(ventas["fecha"])
    ventas["importe"] = ventas["cantidad"] * ventas["precio"]
    return ventas.groupby(ventas["fecha"].dt.to_period('M'))["importe"].sum()

def ventas_por_categoria(ventas, productos):
    """Calcula las ventas totales por categoría."""
    ventas_productos = pd.merge(ventas, productos, on="id_producto")
    ventas_productos["importe"] = ventas_productos["cantidad"] * ventas_productos["precio_x"]
    return ventas_productos.groupby("categoría")["importe"].sum()

def productos_por_categoria(productos):
    """Calcula el número de productos por categoría."""
    categorias = set(productos["categoría"])
    if "vitraux" in categorias:
        vitraux = [producto["nombre"] for producto in productos.to_dict("records") if producto["categoría"] == "vitraux"]
        productos_vitraux = len(vitraux)
    else:
        productos_vitraux = 0
    if "mosaico" in categorias:
        mosaico = [producto["nombre"] for producto in productos.to_dict("records") if producto["categoría"] == "mosaico"]
        productos_mosaico = len(mosaico)
    else:
        productos_mosaico = 0
    return {
        "vitraux": productos_vitraux, 
        "mosaico": productos_mosaico
    }

def clientes_mas_frecuentes(ventas, clientes):
    """Devuelve los clientes por orden de frecuencia."""
    frecuencia = ventas.groupby("id_cliente").size().reset_index(name="cantidad_compras")
    resultado = pd.merge(frecuencia, clientes, on="id_cliente")
    return resultado.sort_values("cantidad_compras", ascending=False)

def detectar_productos_stock_bajo(productos, limite=5):
    """Devuelve los nombres de los productos con stock bajo."""
    productos_stock_bajo = [producto["nombre"] for producto in productos.to_dict("records") if producto["stock"] < limite]
    return productos_stock_bajo

def rango_precios(productos):
    """Devuelve el rango de precios de los productos."""
    precio_minimo = productos["precio"].min()
    precio_maximo = productos["precio"].max()
    return precio_minimo, precio_maximo

def productos_caros_stock_bajo(productos, precio=4500, limite=3):
    """Devuelve los productos sobre un determinado precio y bajo un determinado stock."""
    productos_caros = {producto["nombre"] for producto in productos.to_dict("records") if producto["precio"] >= precio}
    productos_stock_bajo = set(detectar_productos_stock_bajo(productos, limite))
    productos_caros_con_stock_bajo = productos_caros & productos_stock_bajo
    return productos_caros_con_stock_bajo

def productos_por_precio(productos, descendente):
    """Devuelve los productos ordenados por precio."""
    if descendente:
        productos_ordenados = sorted(productos.to_dict("records"), key=lambda producto: producto["precio"], reverse=True)
    else:
        productos_ordenados = sorted(productos.to_dict("records"), key=lambda producto: producto["precio"])
    return [[item["nombre"], item["precio"]] for item in productos_ordenados]

def productos_por_stock(productos, descendente):
    """Devuelve los productos ordenados por stock."""
    if descendente:
        productos_ordenados = sorted(productos.to_dict("records"), key=lambda producto: producto["stock"], reverse=True)
    else:
        productos_ordenados = sorted(productos.to_dict("records"), key=lambda producto: producto["stock"])
    return [[item["nombre"], item["stock"]] for item in productos_ordenados]
    
def ventas_ordenadas(ventas):
    """Ordena las ventas por precio en orden descendente."""
    importe = ventas["cantidad"] * ventas["precio"]
    datos = []
    for i in range(len(importe)):
        datos.append([ventas["id_venta"][i], importe[i]])
    opcion = int(input("Seleccione el algoritmo de ordenamiento: 1 (bubble), 2 (selection), 3 (insertion), 4 (merge), 5 (quick) \n"))
    match opcion:
        case 1:
            ordenamiento = bubble_sort(datos)
        case 2:
            ordenamiento = selection_sort(datos)
        case 3:
            ordenamiento = insertion_sort(datos)
        case 4:
            ordenamiento = mergesort(datos)
        case 5:
            ordenamiento = quicksort(datos, 0, len(datos) - 1)
        case _:
            print("Opción no válida")
    ordenamiento.reverse()
    return ordenamiento

