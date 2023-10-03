from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Creamos una Función que permita conectarnos a la base de datos
def connect_to_db():
    return sqlite3.connect('ucchristus.db')

# Definimos la ruta que se utilizara para obtener los datos por id
# ejemplo ruta http://127.0.0.1:8000/obtener_datos_id/?id=1
@app.get("/obtener_datos_id/{id}")
def obtener_datos(id: int):
    # Nos conectamos a la base de datos con la funcion creada anteriormente
    conexion = connect_to_db()
    cursor = conexion.cursor()

    # Generamos la consulta para obtener los datos filtrados por id
    cursor.execute(f"SELECT * FROM pacientes WHERE id = ?", (id,))
    resultados = cursor.fetchall()

    # Cerramos la conexión a la base de datos
    conexion.close()

    return {"paciente": resultados}

# Definimos la ruta que se utilizara para obtener los datos por email
# ejemplo ruta http://127.0.0.1:8000/obtener_datos_email/?email=sfeasley2@gnu.org
@app.get("/obtener_datos_email/{email}")
def obtener_datos(email: str):
    # Nos conectamos a la base de datos con la funcion creada anteriormente
    conexion = connect_to_db()
    cursor = conexion.cursor()

    # Generamos la consulta para obtener los datos filtrados por id
    cursor.execute(f"SELECT * FROM pacientes WHERE  email= ?", (email,))
    resultados = cursor.fetchall()

    # Cerramos la conexión a la base de datos
    conexion.close()

    return {"paciente": resultados}
