# Ejercicio 11 - Conversión de temperaturas
 
temperatura = float(input("Ingrese una temperatura: "))
escala = int(input("Ingrese una escala (1 -> C, 2 -> F): "))

def convertirTemp(temperatura, escala):
  match escala:
    case 1:
      return (temperatura * 9/5) + 32
    case 2:
      return (temperatura - 32) * 5/9

if escala == 1:
  print("La temperatura convertida de", temperatura, "C es:", convertirTemp(temperatura, escala), "F")
else: 
  print("La temperatura convertida de", temperatura, "F es:", convertirTemp(temperatura, escala), "C")