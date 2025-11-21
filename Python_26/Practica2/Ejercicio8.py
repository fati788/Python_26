"""
Ejercicio 8: Diccionario de longitudes

Dada una lista de strings, crea un diccionario usando comprehension donde las claves sean las palabras y los valores su longitud.

Ejemplo:

palabras = ["Python", "Java", "JavaScript", "C++"]
# {'Python': 6, 'Java': 4, 'JavaScript': 10, 'C++': 3}
"""
palabras = ["Python", "Java", "JavaScript", "C++"]
longitudes = {palabra: len(palabra) for palabra in palabras}
print(longitudes)
#longitudes = {}
#for palabra in palabras:
#    longitudes[palabra] = len(palabra)  # Asignar longitud de la palabra
#print(longitudes)  
