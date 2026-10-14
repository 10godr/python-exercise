import tkinter as tk

# Funciones
def click_boton(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + valor)

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora 🧮")
ventana.geometry("340x450")
ventana.resizable(False, False)
ventana.configure(bg="#1e1e2e")

# Pantalla de entrada
entrada = tk.Entry(ventana, font=("Arial", 20), border=5, relief="sunken", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

# Botones organizados como calculadora real
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0, 4)  # Botón "=" ocupa toda la fila
]

# Crear botones en ventana
for boton in botones:
    if boton[0] == "=":
        tk.Button(
            ventana, text=boton[0], width=34, height=3,
            bg="#3a86ff", fg="white", font=("Arial", 12, "bold"),
            command=calcular
        ).grid(row=boton[1], column=boton[2], columnspan=boton[3], padx=5, pady=5)
    elif boton[0] == "C":
        tk.Button(
            ventana, text=boton[0], width=7, height=3,
            bg="#ef233c", fg="white", font=("Arial", 12, "bold"),
            command=limpiar
        ).grid(row=boton[1], column=boton[2], padx=5, pady=5)
    else:
        tk.Button(
            ventana, text=boton[0], width=7, height=3,
            bg="#2ec4b6", fg="white", font=("Arial", 12, "bold"),
            command=lambda t=boton[0]: click_boton(t)
        ).grid(row=boton[1], column=boton[2], padx=5, pady=5)

ventana.mainloop()
