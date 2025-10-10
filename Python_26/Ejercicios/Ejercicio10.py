### 10. Frecuencia de letras

#Pide al usuario una frase y almacena en un diccionario cuántas veces aparece cada letra.
frase = input("Dime una frase: ")
frase = frase.lower()
letras = {} 
for letra in frase:
    if letra in letras:
        letras[letra] += 1 
        letras[letra] = 1  

print(letras)