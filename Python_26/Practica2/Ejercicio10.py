
#Ejercicio 10: Filtrar números

numeros = [15, 30, 7, 45, 60, 12, 90]
divisibles_por_15 = list(filter(lambda x: x % 15 == 0, numeros))
print(divisibles_por_15)

#divisibles_por_15 = []
#for numero in numeros:
#    if numero % 15 == 0:
#        divisibles_por_15.append(numero)  # Agregar número divisible por 15
#print(divisibles_por_15)
