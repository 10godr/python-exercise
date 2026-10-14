frase = input("Ingrese una palabra o frase: ")

contador = 0
for letra in frase:
    
    while letra == "a" or letra == "A":
        contador += 1
        break

print(f"La cantidad de A es {contador}")