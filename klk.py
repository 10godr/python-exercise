class Usuario:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre}"

    
usuario1 = Usuario("Diego", 19)
print(usuario1.nombre)

print(usuario1.edad)

print(usuario1.saludar())