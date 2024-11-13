#Ejercicio 3 - Calculadora Básica:

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
operacion = int(input("Ingrese una operación (1 -> +, 2 -> -, 3 -> *, 4 -> /): "))

def calculadora(num1, num2, operacion):
  match operacion:
    case 1:
      return num1 + num2
    case 2:
      return num1 - num2
    case 3:
      return num1 * num2
    case 4:
      return num1 / num2

print("El resulado de la operación es: ", calculadora(num1, num2, operacion))


