### 13. Suma de elementos de una matriz

#Crea una matriz (lista de listas) de 2x3 con valores introducidos por el usuario
#  y calcula la suma de todos sus elementos.




matriz = list()
for i in range(0,2):
    matriz.append(list(range(3)))
    for j in range(0,3):
        numero = int(input("Dime un número"))
        print(i,j)
        matriz[i][j] = numero
        
print(matriz)
#Suma de los elementos
contador = 0
for fila in matriz:
    contador += sum(fila) 
print(contador)
