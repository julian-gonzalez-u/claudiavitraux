from .utils import validar_precio, validar_stock
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Producto:
    id_producto: int
    nombre: str
    categoria: str
    precio: float
    stock: int
    def __str__(self):
        return self.nombre
    def actualizar_precio(self, precio):
        if validar_precio(precio):
            self.precio = precio
            print("Precio actualizado")
            return self.precio
        elif not validar_precio(precio):
            return "Precio no válido"
        else:
            self.precio = precio
            return self.precio
    def aumentar_stock(self, mas_stock):
        self.stock += mas_stock
        print("Se agregó stock")
        return self.stock
    def reducir_stock(self, menos_stock):
        if validar_stock(self.stock, menos_stock):
            self.stock -= menos_stock
            print("Se quitó stock")
            return self.stock
        else:
            print("Error")
            return None
    def tiene_stock(self):
        if self.stock > 0:
            return True
        else:
            return False
    def stock_bajo(self):
        if self.stock < 5:
            return True
        else:
            return False

@dataclass
class Cliente:
    id_cliente: int
    nombre: str
    telefono: int
    def __str__(self):
        return self.nombre
    def actualizar_datos(self, nombre, telefono):
        self.nombre = nombre
        if type(telefono) == int:
            self.telefono = telefono
            print("Se actualizaron los datos")
            return self.nombre, self.telefono
        else:
            print("Error. Número de teléfono no válido.")
            return self.nombre
    def mostrar_datos(self):
        return self.nombre, self.telefono

@dataclass
class Venta:
    id_venta: int
    fecha: datetime
    id_cliente: int
    id_producto: int
    cantidad: int
    precio: float
    def __str__(self):
        return f"""
                ID de venta: {self.id_venta} \n
                Fecha: {self.fecha} \n
                ID de cliente: {self.id_cliente} \n
                ID de producto: {self.id_producto}
                """
    def calcular_total(self):
        return self.cantidad * self.precio
    def cantidad_unidades(self):
        return self.cantidad