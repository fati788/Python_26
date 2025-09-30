### 8. Tabla de multiplicar
num = int(input("Introduce un número para ver su tabla de multiplicar: "))
print("Tabla de multiplicar del", num, ":")
for i in range(1, 11):
    print(num, "x", i, "=", num * i)