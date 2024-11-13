# Ejercicio 4 - Determinar tipo de triangulo

l1 = float(input("Ingresa el valor del lado 1: "))
l2 = float(input("Ingresa el valor del lado 2: "))
l3 = float(input("Ingresa el valor del lado 3: "))

if(l1==l2 and l2==l3):
  print("El triangulo es equilatero")
elif(l1==l2 or l1==l3 or l2==l3):
  print("El triangulo es isosceles")
elif(l1!=l2 or l1!=l3 or l2!=l3):
  print("El triangulo es escaleno")
