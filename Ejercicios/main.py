# Ejercicio 22 - Clasificación de triángulos por ángulos

angulo1 = float(input("Ingrese el valor del ángulo 1: "))
angulo2 = float(input("Ingrese el valor del ángulo 2: "))
angulo3 = float(input("Ingrese el valor del ángulo 3: "))

if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
  print("El triángulo es agudo")
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
  print("El triángulo es rectángulo")
elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
  print("El triángulo es obtuso")