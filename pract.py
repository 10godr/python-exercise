# Ejericcios dia 1
# 2. Operaciones
print (5 + 2)
print ( 3 - 7)
print (5 * 15)
print (17 % 31)
print (64 / 4)
print (13 ** 2)
print (64 // 4)

# 3. Cadenas
print("\n-----------------------------------")
print ("Diego")
print ("Rodriguez")
print ('Republica Dominicana')
print ('Estoy disfrutando de 30 dias de Python')

# 4. comprobar tipos de datos
print("-----------------------------------")
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type({'Asabeneh', 'Piton','FInlandia'}))
print(type('Diego'))
print(type('mmg'))

print ("la puta cabra")

#  Número Entero (int)
print("\n-----------------------------------")
edad = 18
print("Edad:", edad)

#  Número Flotante (float)
print("\n-----------------------------------")
altura = 1.83
print("Altura:", altura)

#  Número Complejo (complex)
print("\n-----------------------------------")
numero_complejo = 3 + 4j
print("Número complejo:", numero_complejo)

#  Cadena de texto (str)
print("\n-----------------------------------")
nombre = "Diego"
print("Nombre:", nombre)

#  Booleano (bool)
print("\n-----------------------------------")
es_estudiante = True
print("¿Es estudiante?", es_estudiante)

# list
print("\n-----------------------------------")
frutas = ["manzana", "banana", "uva"]
print("Lista de frutas:", frutas)

#  Tupla (tuple) 
print("\n-----------------------------------")
coordenadas = (10.5, 20.3)
print("Coordenadas:", coordenadas)

#  Conjunto (set) - No permite duplicados, desordenado
print("\n-----------------------------------")
numeros_unicos = {1, 2, 3, 2, 1}
print("Conjunto de números únicos:", numeros_unicos)

#  Diccionario (dict) - Llave:Valor
print("\n-----------------------------------")
persona = {
    "nombre": "Diego",
    "edad": 18,
    "ciudad": "Santo Domingo"
}
print("Diccionario de persona:", persona)

print("\n-----------------------------------")
import math

x1, y1 = 2, 3
x2, y2 = 10, 8

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distancia euclidiana:", distancia)

