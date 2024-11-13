# Ejercicio 5 - Dias de la semana

dia = int(input("Ingrese un numero del 1 al 7: "))
def diasDeLaSemana(dia):
  match dia:
    case 1: return "Lunes"
    case 2: return "Martes"
    case 3: return "Miercoles"
    case 4: return "Jueves"
    case 5: return "Viernes"
    case 6: return "Sabado"
    case 7: return "Domingo"
    
print("El dia de la semana es: ", diasDeLaSemana(dia))