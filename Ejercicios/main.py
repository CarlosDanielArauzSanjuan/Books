# Ejercicio 17 - Calificaciones con bonificación
calificacion = float(input("Ingrese una calificación: "))
tareas = int(input("Realizó tareas adicionales (1 -> Si, 2 -> No): "))
 
if tareas == 1:
  calificacion += calificacion * 0.05
  if calificacion > 100:
    calificacion = 100

print("La calificación es:", calificacion)
