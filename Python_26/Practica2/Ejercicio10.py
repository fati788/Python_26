"""
Ejercicio 10: Filtrar números

Usa filter() con lambda para obtener solo los números que sean divisibles por 3 Y por 5 (es decir, divisibles por 15) de una lista.

Ejemplo:

numeros = [15, 30, 7, 45, 60, 12, 90]
# Resultado: [15, 30, 45, 60, 90]
"""
numeros = [15, 30, 7, 45, 60, 12, 90]
divisibles_por_15 = list(filter(lambda x: x % 15 == 0, numeros))
print(divisibles_por_15)

#divisibles_por_15 = []
#for numero in numeros:
#    if numero % 15 == 0:
#        divisibles_por_15.append(numero)  # Agregar número divisible por 15
#print(divisibles_por_15)
