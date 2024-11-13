# Ejercicio 15 - Cálculo del salario neto

sBruto = int(input("Ingrese su salario bruto: "))
pais = int(input("Ingrese su pais de residencia (1 -> Pais A, 2 -> Pais B, 3 -> Pais C, 4 -> Otro): "))

def calculadoraSalario(sBruto, pais):
  match pais:
    case 1:
      return sBruto - (sBruto * 0.2)
    case 2:
      return sBruto - (sBruto * 0.15)
    case 3:
      return sBruto - (sBruto * 0.1)
    case 4:
      return sBruto - (sBruto * 0.25)

print("El salario Neto es:", calculadoraSalario(sBruto, pais), "$")