#IterativesStructures
# Ejercicio 3 - Factorial de un número
n = int(input("Ingrese un número entero positivo: "))
factorial = 1
for i in range(1, n + 1):
  factorial *= i
print("El factorial de", n, "es:", factorial)

