### 10. Frecuencia de letras

#Pide al usuario una frase y almacena en un diccionario cuántas veces aparece cada letra.
frase = input("Introduce una frase: ")
frecuencia = {}
for letra in frase:
    if letra.isalpha():  # Considera solo letras
        letra = letra.lower()  # Ignora mayúsculas/minúsculas
        if letra in frecuencia:
            frecuencia[letra] += 1
        else:
            frecuencia[letra] = 1
print("Frecuencia de letras:")
for letra, cuenta in frecuencia.items():
    print(letra + ":", cuenta)