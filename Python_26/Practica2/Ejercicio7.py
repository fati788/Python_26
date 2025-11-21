"""
Ejercicio 7: Filtrar palabras

Dada una lista de palabras, crea una nueva lista solo con las palabras que tengan más de 5 letras usando list comprehension.

Ejemplo:

palabras = ["sol", "python", "casa", "programación", "gato", "computadora"]
# Resultado: ['python', 'programación', 'computadora']

"""
#palabras_largas = []   
#for palabra in palabras:
#    if len(palabra) > 5:
#        palabras_largas.append(palabra)  # Agregar palabra a la nueva lista
#print(palabras_largas)
palabras = ["sol", "python", "casa", "programación", "gato", "computadora"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
print(palabras_largas)


