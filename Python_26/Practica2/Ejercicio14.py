
#Ejercicio 14: Coordenadas geográficas

def calcular_distancia_euclidiana(punto1, punto2):
    from math import sqrt
    lat1, lon1 = punto1
    lat2, lon2 = punto2
    distancia = sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)
    return distancia

# Ejemplo de uso
madrid = (40.4168, -3.7038)
barcelona = (41.3851, 2.1734)

# Calcular distancia
dist = calcular_distancia_euclidiana(madrid, barcelona)
print(f"Distancia Madrid-Barcelona: {dist:.2f}")
