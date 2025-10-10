### 15. Diccionario de frecuencias de palabras

#Dada una frase ingresada por el usuario,
#construye un diccionario en el que las claves sean palabras y
#  los valores el número de veces que aparece cada una.
frase = input("Introduce una frase: ")
palabras = frase.split()
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1  
    else:
        frecuencia[palabra] = 1   
        

print("Frequencia de los palabras:" , frecuencia)        