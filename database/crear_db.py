from .conexion import *

with open(BASE_DIR / "schema.sql", "r", encoding="utf-8") as archivo:
    script = archivo.read()

conexion = conectar() 
conexion.executescript(script) 

# ejecutar una consulta para obtener las tablas de la base de datos
cursor = conexion.cursor()
cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
tablas = cursor.fetchall()
print("Tablas de la base de datos:")
for nombre_tabla in ["clientes", "productos", "ventas"]:
    # mostrar las tablas de la base de datos
    print(f'\n--- {nombre_tabla} ---')
    cursor.execute(f'SELECT * FROM {nombre_tabla}')
    for fila in cursor.fetchall():
        print(fila)


# cerrar la conexión
conexion.commit()
conexion.close()

print("Base de datos creada correctamente.")
