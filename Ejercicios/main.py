#IterativesStructures
# Ejercicio 4 - Pares en un rango
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
for i in range(num1, num2 + 1):
  if i % 2 == 0:
    print(i)