# suma los numeros q tu quieras y promedia la suma
suma = 0
contador = 1
cantNumeros= 10


while contador <= cantNumeros:
    numero = int(input(f"Ingrese el número {contador}: "))
    if numero > 0:
        suma += numero
        contador = contador + 1
    else:
        print("Debe ser un número positivo.")


promedio = suma / cantNumeros
print(f"La sumatoria es {suma} y el promedio es {promedio}")