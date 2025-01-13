# Schema del formulari
def formulari_schema(formulari) -> dict:
    return {"":formulari[0],  
            }

# Recor
def formularis_schema(formularis) -> dict:
    return [formulari_schema(formulari) for formulari in formularis]
