import sqlite3
import json

# Creamos la conexión a la base de datos "ucchristus" o
# la creamos en caso de que no exista
conexion = sqlite3.connect('ucchristus.db')

# definimos el nombre del archivo json
archivo_json = "MOCK_DATA.json"

# cargar los datos desde el archivo json
with open(archivo_json, "r") as file:
    data_total = json.load(file)

# definimos la mitad de los registros
mitad = len(data_total) // 2

# cargamos solamente la mitad de los elementos
data = data_total[:mitad]

# Creamos un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Obtenemos las claves del primer elemento del JSON para definir las columnas necesarias para la tabla
primer_elemento = data[0]
columnas = [key for key in primer_elemento.keys()]

# Creamos la tabla con las columnas guardadas en primer_elemento
query_crear_tabla = 'CREATE TABLE IF NOT EXISTS pacientes (id INTEGER PRIMARY KEY, {})'.format(', '.join(['"{}" TEXT'.format(name) for name in columnas[1:]]))
cursor.execute(query_crear_tabla)

# Insertamos los datos del JSON en la tabla
for item in data:
    placeholders = ', '.join(['?' for _ in columnas])
    insert_query = 'INSERT INTO pacientes ({}) VALUES ({})'.format(', '.join(['"{}"'.format(name) for name in columnas]), placeholders)
    cursor.execute(insert_query, tuple(item.values()))

# Guardamos los cambios y cerramos la conexión a la base de datos
conexion.commit()
conexion.close()

print("Tabla creada y datos insertados correctamente.")