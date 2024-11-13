#Ejercicio 21 - Sistema de estacionamiento
horas = int(input("Ingrese el número de horas: "))
costo = 0
  
for i in range(horas):
  if i == 0:
    costo += 5
  elif i >= 1 and i <= 3:
    costo += 4
  elif i > 3:
    costo += 3
 
print("El costo del estacionamiento es:", costo)