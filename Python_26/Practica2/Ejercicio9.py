"""
Funciones Lambda
Ejercicio 9: Ordenar por criterio

Usa una función lambda con sorted() para ordenar una lista de tuplas (nombre, edad, altura) por edad de menor a mayor.

Ejemplo:

personas = [("Ana", 25, 165), ("Juan", 30, 175), ("María", 22, 160)]
# Resultado: [("María", 22, 160), ("Ana", 25, 165), ("Juan", 30, 175)]

"""
personas = [("Ana", 25, 165), ("Juan", 30, 175), ("María", 22, 160)]
personas_ordenadas = sorted(personas, key=lambda x: x[1])
print(personas_ordenadas)
