"""
Ejercicio 3: Contador de palabras

Crea una función que reciba un texto y retorne un diccionario con la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y signos de puntuación).

Ejemplo:

texto = "Python es genial. Python es poderoso y Python es versátil."
contar_palabras(texto)
# {'python': 3, 'es': 3, 'genial': 1, 'poderoso': 1, 'y': 1, 'versátil': 1}
"""
def contar_palabras(texto):
    import string
    from collections import Counter
    # Convertir el texto a minúsculas
    texto = texto.lower()
    # Eliminar signos de puntuación
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    # Dividir el texto en palabras
    palabras = texto.split()
    # Contar la frecuencia de cada palabra
    frecuencia = Counter(palabras)
    # Convertir Counter a diccionario normal
    return dict(frecuencia)
# Ejemplo de uso
texto = "Python es genial. Python es poderoso y Python es versátil."
print(contar_palabras(texto))
    