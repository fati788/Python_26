#Ejercicio 3: Contador de palabras

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
    