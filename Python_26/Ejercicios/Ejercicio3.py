### 3. Números pares en un rango

num_inicio = int(input("Introduce el número de inicio del rango: "))
num_fin = int(input("Introduce el número de fin del rango: "))

print("Números pares entre", num_inicio, "y", num_fin, ":")

for num in range(num_inicio, num_fin + 1):
    if num % 2 == 0:
        print(num)  
