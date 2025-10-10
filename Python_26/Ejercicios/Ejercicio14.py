### 14. Palíndromo

#Solicita al usuario una palabra e indica si es un palíndromo 
# (se lee igual al derecho y al revés).

palabra = input("Dame una palabra: ")
palabra = palabra.lower()

if palabra == palabra[::-1]:
    print("la palabra es palíndromo ")
else:
    print("la palabra es NOOOO palíndromo ")     