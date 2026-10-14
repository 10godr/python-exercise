EdadMinimaAcceso= 18
paisesPermetidios = {"Republica Dominicana", "Colombia"}

edadPersona = int(input("Cual es tu edad? "))

if edadPersona < 18:
    residuo = EdadMinimaAcceso - edadPersona
    print(f"Lo siento, Debes esperar {residuo} años para entrara al ejercito")
    exit()
else:
  paisOrigen = input("Cual es tu pais de origen? ")

  if paisOrigen not in paisesPermetidios:
     print("Lo siento, debes haber nacido en Republica Dominicana o Colombia")
     exit()

  if paisOrigen == "Colombia" and edadPersona < 20:
        print("Lo sentimos, la edad mínima para personas de origen colombiano es 20.")
        exit()
  else:
     print("ok")





