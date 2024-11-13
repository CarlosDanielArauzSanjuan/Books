# Ejercicio 1 - Suma de los primeros n números IterativesStructures
n = int(input("Ingrese un número positivo: "))
suma = 0
for i in range(n + 1):
  suma += i
print("La suma de los primeros", n, "números es:", suma)