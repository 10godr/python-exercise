import sqlite3

conexion = sqlite3.connect("database.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    contraseña TEXT NOT NULL
)
""")

# Usuario de prueba
cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
               ("admin", "1234"))

conexion.commit()
conexion.close()

print("Base de datos creada")
