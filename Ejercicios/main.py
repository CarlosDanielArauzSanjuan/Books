# Ejercicio 14 - Adivinanza de letras

letra = input("Adivina la letra: ")
secreta = "f"

def adivinarLetra(letra):
  match letra:
    case "a": return "Letra incorrecta"
    case "b": return "Letra incorrecta"
    case "c": return "Letra incorrecta"
    case "d": return "Letra incorrecta"
    case "e": return "Letra incorrecta"
    case "f": return "Adivinaste"
    case "g": return "Letra incorrecta"
    case "h": return "Letra incorrecta"
    case "i": return "Letra incorrecta"
    case "j": return "Letra incorrecta"
    case "k": return "Letra incorrecta"
    case "l": return "Letra incorrecta"
    case "m": return "Letra incorrecta"
    case "n": return "Letra incorrecta"
    case "o": return "Letra incorrecta"
    case "p": return "Letra incorrecta"
    case "q": return "Letra incorrecta"
    case "r": return "Letra incorrecta"
    case "s": return "Letra incorrecta"
    case "t": return "Letra incorrecta"
    case "u": return "Letra incorrecta"
    case "v": return "Letra incorrecta"
    case "w": return "Letra incorrecta"
    case "x": return "Letra incorrecta"
    case "y": return "Letra incorrecta"
    case "z": return "Letra incorrecta"

print(adivinarLetra(letra), "la letra era:", secreta)