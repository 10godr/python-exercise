from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def conectar_db():
    return sqlite3.connect("database.db")

@app.route("/", methods=["GET", "POST"])
def login():
    mensaje = ""

    if request.method == "POST":
        usuario = request.form.get("usuario")
        password = request.form.get("password")

        print("DEBUG -> usuario:", usuario)
        print("DEBUG -> password:", password)

        try:
            conexion = conectar_db()
            cursor = conexion.cursor()

            cursor.execute(
                "SELECT * FROM usuarios WHERE usuario=? AND password=?",
                (usuario, password)
            )

            resultado = cursor.fetchone()
            conexion.close()

            print("DEBUG -> resultado:", resultado)

            if resultado:
                mensaje = "✅ Login correcto"
            else:
                mensaje = "❌ Usuario o contraseña incorrectos"

        except Exception as e:
            mensaje = "⚠️ Error interno"
            print("ERROR REAL:", e)

    return render_template("login.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
