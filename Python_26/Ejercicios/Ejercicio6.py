### 6. Máximo y mínimo de una lista
numeros = []

for i in range(5):
    num = int(input("Introduce un número: "))
    numeros.append(num) 
maximo = max(numeros)
minimo = min(numeros)

print("El número máximo es:", maximo)
print("El número mínimo es:", minimo)