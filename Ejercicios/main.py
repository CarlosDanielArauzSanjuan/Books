# Ejercicio 20 - Conversión de calificaciones numéricas a letras
 
calificacion = int(input("Ingrese una calificación: "))

def convertirCalificacion(calificacion):
  match calificacion:
    case _ if calificacion < 60: return "F"
    case _ if calificacion < 70: return "D"
    case _ if calificacion < 80: return "C"
    case _ if calificacion < 90: return "B"
    case _ if calificacion <= 100: return "A"
    
print("La calificación es:", convertirCalificacion(calificacion))
