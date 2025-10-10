#19. Lista de palabras únicas
frase = input("Dame una frase: ")
palabras = frase.split()
lista = []
for palabra in palabras:
    if palabra not in lista:
        lista.append(palabra)

print(lista)        