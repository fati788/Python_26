
#Ejercicio 11: Mapeo de temperaturas

celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)
#fahrenheit = []
#for c in celsius:
#    f = (c * 9/5) + 32  # Convertir a Fahrenheit
#    fahrenheit.append(f)
#print(fahrenheit)