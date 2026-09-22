from python.cargar_json import analizar_datos
from python.export_data import *
from python.import_data import *
from python.search import *

while True:
    try:
        print(f"""{"-" * 10} \n
            0: Salir
            1: Agregar un producto
            2: Agregar clientes
            3: Registrar una venta
            4: Cargar datos a la base de datos
            5: Buscar un producto en la base de datos
            6: Análisis de datos
        """)
        opcion = int(input("Seleccione una opción: \n"))
        match opcion:
            case 0:
                print("Cerrando el programa...")
                break
            case 1:
                crear_producto()
            case 2:
                crear_clientes()
            case 3:
                registrar_venta()
            case 4:
                importar_datos()
            case 5:
                buscar_producto()
            case 6:
                analizar_datos()
            case _:
                print("Opción inválida.")
    except ValueError:
        print("Debe introducir un número.")