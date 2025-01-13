import mysql.connector

def db_client():
    try:
        dbname = "formulario"
        user = "root"
        password = "1234"
        host = "127.0.0.1"
        port = "3307"
        collation = "utf8mb4_general_ci"
        
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=dbname,
            collation=collation
        )
        
        print("Connexió exitosa!: ", connection)
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió: {e}"}
    
db_client()