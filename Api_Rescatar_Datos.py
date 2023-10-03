from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# Configuramos el CORS para permitir solicitudes del html
origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creamos una Función que permita conectarnos a la base de datos
def connect_to_db():
    return sqlite3.connect('ucchristus.db')

# Definimos la ruta que se utilizara para obtener los datos por id o email
# ejemplo ruta http://127.0.0.1:8000/obtener_datos/sfeasley2@gnu.org
@app.get("/obtener_datos/{filtro}")
def obtener_datos(filtro: str):
    # Nos conectamos a la base de datos con la funcion creada anteriormente
    conexion = connect_to_db()
    cursor = conexion.cursor()

    # Generamos la consulta para obtener los datos filtrados por id
    cursor.execute(f"SELECT * FROM pacientes WHERE id = ? or email = ?", (filtro,filtro))
    resultados = cursor.fetchall()

    # Cerramos la conexión a la base de datos
    conexion.close()

    return {"paciente": resultados}
