print("Verifique si un año es bisiesto o no")

year = int(input("¿Qué año quieres verificar? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"El año {year} es un año bisiesto")
    else:
      print (f"El año {year} no es un año bisiesto")
  else:
    print(f"El año {year} es un año bisiesto")
else:
  print (f"El año {year} no es un año bisiesto")