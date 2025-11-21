"""
Ejercicio 11: Mapeo de temperaturas

Convierte una lista de temperaturas en Celsius a Fahrenheit usando map() y lambda. La fórmula es: F = (C × 9/5) + 32

Ejemplo:

celsius = [0, 10, 20, 30, 40]
# Resultado: [32.0, 50.0, 68.0, 86.0, 104.0]

"""
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)
#fahrenheit = []
#for c in celsius:
#    f = (c * 9/5) + 32  # Convertir a Fahrenheit
#    fahrenheit.append(f)
#print(fahrenheit)