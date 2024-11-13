# Ejercicio 16 - Cálculo del tiempo de viaje

import math
distancia = float(input("Ingrese la distancia en km: "))
velocidad = float(input("Ingrese la velocidad en km/h: "))
tiempo = distancia / velocidad
decimal, entero = math.modf(tiempo)
tiempoMinutos = decimal * 60
print("El tiempo de viaje es:", entero, "horas y", round(tiempoMinutos), "minutos")
if velocidad > 120:
  print("Advertencia, no exceda los limites de velocidad")
