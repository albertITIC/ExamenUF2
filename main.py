from fastapi import FastAPI
from conn import db_client
from pydantic import BaseModel

app = FastAPI()


# Base Model de la nostra base de dades
class formulario (BaseModel):
    nombre : str
    apellido: str
    correElectronico : str
    descripcion : str | None
    curso : int
    año : int
    direccion : str
    codigoPostal : int | None
    password : str
    
# Endpoints del formulari
# La ruta principal de la API
@app.get("/")
def read_root():
    return {"API de Formulari"}

