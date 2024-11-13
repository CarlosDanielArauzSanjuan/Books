 #Ejercicio 6 - Adivinanza
from random import *

num = 0
aleatorio = randint(1, 10)
while(num != aleatorio):
  num = int(input("Adivina el numero del 1 al 10: "))
  if(num < aleatorio):
    print("El numero es mayor")
  else:
    print("El numero es menor")
    
print("Adivinaste el numero, era:", aleatorio)