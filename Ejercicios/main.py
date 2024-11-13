#IterativesStructures
Ejercicio 7 - Suma de numeros pares hasta introducir un impar
num = int(input("Ingrese un número entero positivo: "))
suma = 0
while num % 2 == 0:
  suma += num
  num = int(input("Ingrese un número entero positivo: "))
print("La suma de los números pares es:", suma)
