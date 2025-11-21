#Ejercicio 8: Diccionario de longitudes

palabras = ["Python", "Java", "JavaScript", "C++"]
longitudes = {palabra: len(palabra) for palabra in palabras}
print(longitudes)
#longitudes = {}
#for palabra in palabras:
#    longitudes[palabra] = len(palabra)  # Asignar longitud de la palabra
#print(longitudes)  
