# Schema del formulari
def formulari_schema(formulari) -> dict:
    return {"nombre":formulari[0],  
            "apellido":formulari[1],
            "correoElectronico":formulari[2],
            "descripcion": formulari[3],
            "curso": formulari[4],
            "año": formulari[5],
            "direccion": formulari[6],
            "codigoPostal": formulari[7],
            "password":formulari [8]
            }

# Recor
def formularis_schema(formularis) -> dict:
    return [formulari_schema(formulari) for formulari in formularis]