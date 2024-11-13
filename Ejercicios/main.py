#IterativesStructures
# Ejercicio 2 - Contador de vocales de una cadena
cadena = input("Ingrese una cadena: ")
contador = 0
for caracter in cadena:
  if caracter.lower() in "aeiou":
    contador += 1
print("La cadena tiene", contador, "vocales")
