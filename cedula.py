#Realiza un programa que te pregunte la edad y el año de nacimiento y a partir de esa informacion te diga si puedes sacar tu cedula o no. 

fechaNacimiento = float (input(" ingresa tu fecha de nacimiento: "))
print("Muy bien")
añoActual = 2025

edad = int(añoActual - fechaNacimiento)
print("Tu edad es", edad )

if edad >= 18:
  print("Puedes sacar tu cedula")

else:
    print("No puedes sacar tu cedula")
