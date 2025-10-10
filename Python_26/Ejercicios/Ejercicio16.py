### 16. Lista ordenada

#Pide al usuario ingresar varios números, guárdalos en una lista y muestra:

numeros = []

for i in range(1,6):
    numero = int(input("Dame un numero: "))
    numeros.append(numero)
#- La lista original.
print(numeros)    
#- La lista ordenada ascendentemente.  
numeros.sort()
print(numeros)
#- La lista ordenada descendentemente.  
numeros.sort(reverse=True)
print(numeros)