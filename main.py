from fastapi import FastAPI, HTTPException
from conn import db_client
from pydantic import BaseModel
from db_formulario import create_Usuari 

app = FastAPI()

# Base Model de la nostra base de dades
class formulario (BaseModel):
    nombre : str
    apellido: str
    correoElectronico : str
    descripcion : str | None
    curso : str
    año : int
    direccion : str
    codigoPostal : int | None
    password : str
    
# Endpoints del formulari
# La ruta principal de la API
@app.get("/")
def read_root():
    return {"API de Formulari"}

# Endpoint per crear un nou usuari
@app.post("/formulari/add_user")
async def crear_usuari(data: formulario):
    try:
        # Truque'm a la funció per crear l'usuari i pasem les dades
        result = create_Usuari(
            data.nombre, 
            data.apellido, 
            data.correoElectronico, 
            data.descripcion, 
            data.curso, 
            data.año, 
            data.codigoPostal, 
            data.password
        )
        
        # Si resulta que el codi és igual a 1 retornem la resposta del resultat
        if result["status"] == 1:
            return result
        else:
            # Llancem una excepció HTTP
            raise HTTPException(status_code=400, detail=result["message"])
    
    except Exception as e:
        # En cas de qualsevol altre inesperat
        raise HTTPException(status_code=500, detail=f"Error intern: {e}")    
