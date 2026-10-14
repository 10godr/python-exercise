# calculadora picante
def calculadora():
    print("----calculadora psicopata que suma, resta, divide y multiplica")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (x)")
    print("4. DIvidir (/)")
    print("5. Salir")
    
    while True:
        try:
            opcion = int(input("Elija una opcion del 1 al 5: "))
        except ValueError:
            print(" Debes ingresar un número del 1 al 5.")
            continue

        if opcion == 5:
            print("tato entonce")
            break

        if opcion in [1, 2, 3, 4]:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Debes ingresar números válidos.")
                continue

            if opcion == 1:
                resultado = num1 + num2
                print(f" Resultado: {num1} + {num2} = {resultado}")

            elif opcion == 2:
                resultado = num1 - num2
                print(f" Resultado: {num1} - {num2} = {resultado}")

            elif opcion == 3:
                resultado = num1 * num2
                print(f" Resultado: {num1} * {num2} = {resultado}")

            elif opcion == 4:
                if num2 == 0:
                    print("Error: No se puede dividir entre 0 ñame")
                    continue
                resultado = num1 / num2
                print(f" Resultado: {num1} / {num2} = {resultado}")

            elif opcion != {1,2,3,4,5}:
                print("del 1 al 5 ñame")

        print("\n")
        print("-----------------------------------")
        print("¿Qué operación deseas ahora?")
        print("1) Sumar | 2) Restar | 3) Multiplicar | 4) Dividir | 5) Salir")

calculadora()
