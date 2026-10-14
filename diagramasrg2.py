# Calcular y mostrar salario semanal a pagar a un empleado que trabajó X horas, donde el valor de X debe leerse.  El precio por hora es de RD$550.00 cuando se trabaja hasta 40 horas.  Las horas trabajadas por encima de 40 se considerarán como HORAS EXTRAS y el precio de las mismas es un 75% por encima del precio de la hora normal. 

horasTrabajadas = int(input("Cuantas horas trabajo? "))

if horasTrabajadas > 40:
    precioHora = 550 * 0.75
    salarioSemanal = horasTrabajadas * precioHora
    print(f"Su salario es de RD${salarioSemanal}")

else:
    precioHora = 550
    salarioSemanal= horasTrabajadas * precioHora
    print(f"Su salario es de RD${salarioSemanal}")
