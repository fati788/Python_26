
#Ejercicio 6: Números al cuadrado

cuadrados_pares = [x**2 for x in range(1, 51) if x % 2 == 0]
print(cuadrados_pares)
#cuadrados_pares = []

#for x in range(1, 51):
#    if x % 2 == 0:
#        cuadrados_pares.append(x**2)    # Agregar el cuadrado del número par a la lista
#print(cuadrados_pares)