# Ejercicio 13 - Comparación de 3 números

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))

if num1 > num2 and num1 > num3:
  print("El numero", num1, "es el mayor")
elif num2 > num1 and num2 > num3:
  print("El numero", num2, "es el mayor")
else:
  print("El numero", num3, "es el mayor")
