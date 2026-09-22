from database.queries import *
from python.analysis import *
from python.utils import *
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent

def analizar_datos():
    """Análisis de todos los datos."""
    productos = obtener_productos()
    clientes = obtener_clientes()
    ventas = obtener_ventas()
    total = calcular_ventas_totales(ventas)
    promedio = calcular_promedio_venta(ventas)
    mas_vendido = producto_mas_vendido(ventas)
    menos_vendido = producto_menos_vendido(ventas)
    por_mes = ventas_por_mes(ventas)
    por_categoria = ventas_por_categoria(ventas, productos)
    clientes_frecuentes = clientes_mas_frecuentes(ventas, clientes)
    stock_bajo = detectar_productos_stock_bajo(productos, 4)
    rango = rango_precios(productos)
    productos_categorias = productos_por_categoria(productos)
    caros_stock_bajo = productos_caros_stock_bajo(productos)
    orden_precio = productos_por_precio(productos, True)    
    orden_stock = productos_por_stock(productos, True)
    orden_ventas = ventas_ordenadas(ventas)
    resultados = {
        "ventas_totales": total,
        "promedio_venta": promedio,
        "mas_vendido": mas_vendido,
        "menos_vendido": menos_vendido,
        "ventas_por_mes": por_mes,
        "ventas_por_categoria": por_categoria,
        "clientes_frecuentes": clientes_frecuentes,
        "productos_stock_bajo": stock_bajo,
        "rango_precios": rango,
        "productos_por_categoria": productos_categorias,
        "productos_caros_stock_bajo": caros_stock_bajo,
        "productos_por_precio": orden_precio,
        "productos_por_stock": orden_stock,
        "ventas_ordenadas": orden_ventas
        }
    resultados = convertir_datos(resultados)
    with open(BASE_DIR / "json/resultado.json", "w", encoding="utf-8") as archivo:
        json.dump(resultados, archivo, ensure_ascii=False, indent=4)
    print("Datos analizados correctamente.")

