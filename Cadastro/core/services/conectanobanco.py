import psycopg


def conectar():
    return psycopg.connect(
        host="localhost",
        port=5432,
        dbname="postgres",
        user="postgres",
        password="123123"
    )

print("Conectado com sucesso!")