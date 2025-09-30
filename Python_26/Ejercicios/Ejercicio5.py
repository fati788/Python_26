# Lista invertida
#Crea una lista con 5 números introducidos por el usuario y luego muéstrala invertida.
numeros = []
for i in range(5):
    num = int(input("Introduce un número: "))
    numeros.append(num)
numeros_invertidos = numeros[::-1]
print("Lista invertida:", numeros_invertidos)