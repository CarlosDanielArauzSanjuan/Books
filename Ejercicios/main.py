# Ejercicio 18 - Evaluación de créditos universitarios

num_materias = int(input("Ingrese el numero de materias cursadas: "))
aprobadas = 0

for i in range(num_materias):
  nota = int(input("Ingrese la nota de la materia: "))
  if nota >= 60:
    aprobadas += 1
    print("La materia fue aprobada")
  else:
    print("La materia fue reprobada")
    
print("La cantidad de materias aprobadas fue:", aprobadas)
print("El número total de créditos es:", aprobadas * 3)