print("Hay tres opciones: \n")

print("1. De Celsius a Farenheit")
print("2. De Farenheit a Celsius \n")
print("3. Salir...")

while True:
    answer = input("Elige una opción: (1, 2 o 3): ")

    if answer == "1":
        celsius = float (input("Ingrese los grados(En Celsius): "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"La temperatura en Fahrenheit es: {fahrenheit}°F")
    

    elif answer == "2":
        fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"La temperatura en Celsius es: {celsius}°C")
    
    elif answer == "3":
        print("tato miop entonce cuidese")
        break

    else:
        print("Opción inválida, elija 1 o 2 o 3 miop")





