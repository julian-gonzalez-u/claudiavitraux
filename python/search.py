from python.algoritmos.searching import *
from python.algoritmos.quicksort import quicksort
from database.queries import *

def buscar_producto():
    """Busca un producto."""
    productos = quicksort(list(obtener_productos()["id_producto"]), 0, len(list(obtener_productos()["id_producto"])) - 1)
    intentos = 0
    max_intentos = 3
    while intentos < max_intentos:
        try:
            # pedir el ID del producto como un número entero
            id_producto = int(input("Ingresá el ID del producto: \n"))
        except ValueError:
            # si el ID no es un número, mensaje de error, se suma un intento y se vuelve a ejecutar el ciclo
            print("El ID debe ser un número.")
            intentos += 1
            continue
        opcion = input("Ingrese el tipo de búsqueda a realizar: lineal o binaria \n")
        match opcion:
            case "lineal":
                indice = busqueda_lineal(productos, id_producto)
            case "binaria":
                indice = busqueda_binaria(productos, id_producto)
            case _:
                print("Opción no reconocida")
                continue
        producto = productos[indice]
        if producto is not None and indice != -1:
            # si se halló el producto, imprimir mensaje y salir del ciclo
            print("Producto encontrado")
            break
        print("No se encontró el producto.")
        intentos += 1
    else:
        print("Se agotaron los intentos.")
