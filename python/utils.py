import pandas as pd # type: ignore
import numbers
from datetime import datetime

def formatear_fecha(fecha):
    try:
        fecha = datetime.strptime(fecha, "%d/%m/%Y")
    except ValueError:
        return "Fecha inválida"
    return fecha

def validar_precio(precio):
    if type(precio) == int or type(precio) == float:
        if precio >= 0:
            return True
        else:
            return False
    elif type(precio) == str:
        try:
            precio = float(precio)
            return True
        except:
            return False
    else:
        return False

def validar_stock(stock, menos_stock):
    if type(menos_stock) == int and menos_stock <= stock:
        return True
    else:
        return False
    
def convertir_datos(datos):
    if isinstance(datos, pd.DataFrame):
        return convertir_datos(datos.to_dict(orient="records"))
    elif isinstance(datos, pd.Series):
        return convertir_datos(datos.to_dict())
    elif isinstance(datos, pd.Period):
        return str(datos)
    elif isinstance(datos, dict):
        return {
            convertir_datos(clave): convertir_datos(valor) for clave, valor in datos.items()
        }
    elif isinstance(datos, list) or isinstance(datos, tuple) or isinstance(datos, set):
        return [convertir_datos(elemento) for elemento in datos]
    elif isinstance(datos, numbers.Integral):
        return int(datos)
    elif isinstance(datos, numbers.Real):
        return float(datos)
    return datos
