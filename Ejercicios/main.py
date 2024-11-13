# Ejercicio 12 - Calculadora de IMC

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en m: "))
imc = peso / (altura**2)
if imc < 18.5:
  print("Bajo peso")
elif imc >= 18.5 and imc <= 24.9:
  print("Peso normal")
elif imc >= 25 and imc <= 29.9:
  print("Sobrepeso")
else:
  print("Obesidad")