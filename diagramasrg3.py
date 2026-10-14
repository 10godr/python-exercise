precioNormal = 1300.00

print("Bienvenidos a nuestro parque de diversiones,  el precio normal de entrada es de RD$1,300.00 por persona.  Para grupos de 2 a 10 estudiantes el precio especial es de RD$1,000.00, para grupos de 11 a 20 estudiantes el precio es de RD$800 y para grupos de más de 20 estudiantes el precio es de RD$600.  Adicionalmente, hay un descuento de 10% para grupos de más de 30 estudiantes. ")
while True:
    try:
        cantidadEstudiantes = int(input("¿Cuántos estudiantes son? "))
        
        if cantidadEstudiantes < 1:
            print("Obviamente tiene que ser una cantidad positiva, vuelva a intentarlo.")
        elif cantidadEstudiantes > 60:
            print("Lo sentimos, no se aceptan más de 60 estudiantes.")
        else:
            break
    except ValueError:
        print("Obviamente debe ser un numero entero. Vuelva a intentarlo.")



if cantidadEstudiantes == 1:
    precioTotal = precioNormal

elif 2 <= cantidadEstudiantes <=10:
    precioEspecial = 1000.00
    precioTotal = cantidadEstudiantes * precioEspecial

elif 11 <= cantidadEstudiantes <= 20:
    precioEspecial = 800.00
    precioTotal = cantidadEstudiantes * precioEspecial

elif cantidadEstudiantes > 20:
    precioEspecial = 600.00
    precioTotal = cantidadEstudiantes * precioEspecial

elif 30 <= cantidadEstudiantes <= 60:
    precioEspecial = 600.00 - (600.00 * 0.1)
    precioTotal = cantidadEstudiantes * precioEspecial

print(f"El precio total a pagar es: RD${precioTotal:.1f}")











