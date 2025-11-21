
#Ejercicio 1: Calculadora de estadísticas

def calcular_estadisticas(numeros):
    from collections import Counter
    n = len(numeros)
    media = sum(numeros) / n
    
    numeros_ordenados = sorted(numeros)
    if n % 2 == 0:
        mediana = (numeros_ordenados[n//2 - 1] + numeros_ordenados[n//2]) / 2
    else:
        mediana = numeros_ordenados[n//2]
    
    contador = Counter(numeros)
    max_frecuencia = max(contador.values())
    modas = [num for num, freq in contador.items() if freq == max_frecuencia]
    moda = modas[0] if len(modas) == 1 else modas
    
    return {
        'media': round(media, 2),
        'mediana': mediana,
        'moda': moda
    }
# Ejemplo de uso
numeros = [1, 2, 2, 3, 4, 5, 5, 5, 6]
resultado = calcular_estadisticas(numeros)
print(resultado) 