from flask import Flask, jsonify, request # type: ignore
from database.queries import *

app = Flask(__name__)

solicitudes_pendientes = []
siguiente_id_solicitud = 1

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API de ventas funcionando"
    })

@app.route("/productos")
def productos():
    df = obtener_productos()
    return jsonify(df.to_dict(orient="records"))

@app.route("/clientes")
def clientes():
    df = obtener_clientes()
    return jsonify(df.to_dict(orient="records"))

@app.route("/ventas")
def ventas():
    df = obtener_ventas()
    return jsonify(df.to_dict(orient="records"))

@app.route("/ventas", methods=["POST"])
def solicitar_venta():
    global siguiente_id_solicitud
    datos = request.get_json()
    if datos is None:
        return jsonify({
        "error": "Se requiere información en formato JSON"
        }), 400
    id_cliente = datos.get("id_cliente")
    id_producto = datos.get("id_producto")
    cantidad = datos.get("cantidad")
    if id_cliente is None or id_producto is None or cantidad is None:
        return jsonify({
            "error": "Faltan datos de la venta"
        }), 400
    if not isinstance(cantidad, (int, float)) or isinstance(cantidad, bool):
        return jsonify({
            "error": "La cantidad debe ser un número"
        }), 400
    if cantidad <= 0:
        return jsonify({
            "error": "La cantidad debe ser mayor que cero"
        }), 400
    solicitud = {
        "id_solicitud": siguiente_id_solicitud,
        "id_cliente": id_cliente,
        "id_producto": id_producto,
        "cantidad": cantidad,
        "estado": "pendiente"
    }
    solicitudes_pendientes.append(solicitud)
    siguiente_id_solicitud += 1
    return jsonify({
        "mensaje": "Solicitud de venta recibida",
        "solicitud": solicitud
    }), 201

@app.route("/ventas/pendientes", methods=["GET"])
def obtener_solicitudes_pendientes():
    pendientes = []
    for solicitud in solicitudes_pendientes:
        if solicitud["estado"] == "pendiente":
            pendientes.append(solicitud)
    return jsonify(pendientes)

@app.route("/ventas/solicitudes/<int:id>/aceptar", methods=["PUT"])
def aceptar_solicitud(id):
    for solicitud in solicitudes_pendientes:
        if solicitud["id_solicitud"] == id:
            if solicitud["estado"] != "pendiente":
                return jsonify({
                    "error": "La solicitud ya fue procesada"
                }), 400
            solicitud["estado"] = "aceptada"
            return jsonify({
                "mensaje": "Solicitud aceptada",
                "solicitud": solicitud
            }), 200
    return jsonify({
        "error": "Solicitud no encontrada"
    }), 404

@app.route("/ventas/solicitudes/<int:id>/rechazar", methods=["PUT"])
def rechazar_solicitud(id):
    for solicitud in solicitudes_pendientes:
        if solicitud["id_solicitud"] == id:
            if solicitud["estado"] != "pendiente":
                return jsonify({
                    "error": "La solicitud ya fue procesada"
                }), 400
            solicitud["estado"] = "rechazada"
            return jsonify({
                "mensaje": "Solicitud rechazada",
                "solicitud": solicitud
            }), 200
    return jsonify({
        "error": "Solicitud no encontrada"
    }), 404

@app.route("/productos/<int:id>")
def producto(id):
    df = obtener_productos()
    producto = df[df["id_producto"] == id]
    if producto.empty:
        return jsonify({
            "error": "Producto no encontrado"
        }), 404
    return jsonify(producto.to_dict(orient="records")[0])

@app.route("/buscar_productos")
def buscar_productos():
    nombre = request.args.get("nombre")
    df = obtener_productos()
    if nombre:
        df = df[df["nombre"].str.contains(nombre, case=False, na=False)]
    return jsonify(df.to_dict(orient="records"))


if __name__ ==  "__main__":
    app.run(debug=True)
