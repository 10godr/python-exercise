# # 4) Calcular y mostrar salario semanal a pagar a un empleado que trabajó X horas, donde el valor de X debe leerse.  El precio por hora es de RD$550.00.
precioHora = 550
horasTrabajadas = int(input("Cuantas horas trabajó? "))

salario = horasTrabajadas * precioHora

print(f"El salario del empleado es de RD${salario}")