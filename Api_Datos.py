from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pydantic import BaseModel

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

class Paciente(BaseModel):
    nombre: str
    apellido: str
    correo: str
    genero: str
    plan: str
    telefono: str

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

    # Retornamos el paciente
    return {"paciente": resultados}

# Definimos la ruta que se utilizara para insertar datos a la base de datos
@app.post("/insertar_paciente/")
def insertar_paciente(paciente: Paciente):
    # Nos conectamos a la base de datos con la funcion creada anteriormente
    conexion = connect_to_db()
    cursor = conexion.cursor()
    try:
        # Extraemos el ultimo id existente en la base de datos y le sumamos 1
        cursor.execute("SELECT MAX(id) FROM pacientes")
        max_id = cursor.fetchone()[0]
        nuevo_id = str(max_id + 1) if max_id is not None else "1"

        # Ejecumanos la consulta para la inyeccion de los datos 
        cursor.execute(
            "INSERT INTO pacientes(id, first_name, last_name, email, gender, [Plan de Salud], phone) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (nuevo_id, paciente.nombre, paciente.apellido, paciente.correo, paciente.genero, paciente.plan, paciente.telefono)
        )
        
        # Cargamos los cambios y cerramos la conexion a la base de datos 
        conexion.commit()
        conexion.close()

        # Retornamos un mensaje con el id del paciente insertado
        return {"mensaje": f"Paciente insertado con éxito, ID: {nuevo_id}"}
    except Exception as e:
        conexion.rollback()
        # Controlamos el error 
        return HTTPException(status_code=500, detail=f"Error al insertar el paciente: {str(e)}")