import tkinter as tk
from tkinter import ttk
import requests # type: ignore

URL_PENDIENTES = "http://127.0.0.1:5000/ventas/pendientes"

def obtener_solicitudes():
    respuesta = requests.get(URL_PENDIENTES)
    if respuesta.status_code == 200:
        return respuesta.json()
    return []

def actualizar_tabla():
    for elemento in tabla.get_children():
        tabla.delete(elemento)
    solicitudes = obtener_solicitudes()
    for solicitud in solicitudes:
        tabla.insert("", tk.END, values=(
            solicitud["id_solicitud"],
            solicitud["id_cliente"],
            solicitud["id_producto"],
            solicitud["cantidad"]
        ))

def aceptar_solicitud():
    seleccion = tabla.selection()
    if not seleccion:
        print("No se seleccionó ninguna solicitud")
        return
    elemento = tabla.item(seleccion[0])
    id_solicitud = elemento["values"][0]
    url = f'http://127.0.0.1:5000/ventas/solicitudes/{id_solicitud}/aceptar'
    respuesta = requests.put(url)
    if respuesta.status_code == 200:
        print("Solicitud aceptada")
        actualizar_tabla()
    else:
        print("Error al aceptar la solicitud")

def rechazar_solicitud():
    seleccion = tabla.selection()
    if not seleccion:
        print("No se seleccionó ninguna solicitud")
        return
    elemento = tabla.item(seleccion[0])
    id_solicitud = elemento["values"][0]
    url = f'http://127.0.0.1:5000/ventas/solicitudes/{id_solicitud}/rechazar'
    respuesta = requests.put(url)
    if respuesta.status_code == 200:
        print("Solicitud rechazada")
        actualizar_tabla()
    else:
        print("Error al rechazar la solicitud")

ventana = tk.Tk()
ventana.title("Administración de ventas")
ventana.geometry("600x400")

titulo = ttk.Label(ventana, text="Solicitudes de ventas pendientes")
titulo.pack(pady=10)

tabla = ttk.Treeview(ventana, columns=("id", "cliente", "producto", "cantidad"), show="headings")
tabla.heading("id", text="ID")
tabla.heading("cliente", text="Cliente")
tabla.heading("producto", text="Producto")
tabla.heading("cantidad", text="Cantidad")

tabla.pack(fill="both", expand=True, padx=10, pady=10)

boton_actualizar = ttk.Button(ventana, text="Actualizar", command=actualizar_tabla)
boton_actualizar.pack(pady=10)

boton_aceptar = ttk.Button(ventana, text="Aceptar solicitud", command=aceptar_solicitud)
boton_aceptar.pack(pady=5)

boton_rechazar = ttk.Button(ventana, text="Rechazar solicitud", command=rechazar_solicitud)
boton_rechazar.pack(pady=5)

ventana.mainloop()
