# Ejercicio 10 - Clasificacón de notas

nota = int(input("Ingrese una nota: "))
if nota >= 0 and nota <= 59:
  print("La calificación es F")
elif nota >= 60 and nota <= 69:
  print("La calificación es D")
elif nota >= 70 and nota <= 79:
  print("La calificación es C")
elif nota >= 80 and nota <= 89:
  print("La calificación es B")
else:
  print("La calificación es A")
