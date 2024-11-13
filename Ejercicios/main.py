# Ejercicio 9 - Clasificacón de edades

edad = int(input("Ingrese una edad: "))
if edad >= 0 and edad <=12:
  print("La persona es un niño")
elif edad >= 13 and edad <= 17:
  print("La persona es un adolescente")
elif edad >= 18 and edad <= 64:
  print("La persona es un adulto")
else: 
  print("La persona es un anciano")