#Ejercicio 9: Ordenar por criterio

personas = [("Ana", 25, 165), ("Juan", 30, 175), ("María", 22, 160)]
personas_ordenadas = sorted(personas, key=lambda x: x[1])
print(personas_ordenadas)
