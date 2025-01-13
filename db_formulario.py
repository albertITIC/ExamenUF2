# Fitxer funcions
from conn import db_client

# POST - Crear un nou usuari
def create_Usuari(nombre, apellido, correoElectronico, descripcion, curso, año, codigoPostal, password):
    try:
        conn = db_client()
        cur = conn.cursor()
        
        # Consulta SQL per insertar un nou usuari a la base de dades
        query = "INSERT INTO formulario (nombre, apellido, correoElectronico, descripcion, curso, año, codigoPostal, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        values = (nombre, apellido, correoElectronico, descripcion, curso, año, codigoPostal, password) 
        cur.execute(query, values)
        
        # Confirmem que les dades hagin sigut guardades
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "missatge": f"Error de connexió:{e}"}
    finally:
        conn.close()
        
    # Informo al usuari que s'ha creat correctament
    return {"status": 200, "missatge": "Usuari creat exitosament."}