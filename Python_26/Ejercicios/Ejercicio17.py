# 17. Producto escalar de dos listas

#Solicita dos listas de números de igual longitud y calcula el producto escalar 
#(sumando el producto de los elementos en la misma posición).
numeros1 = []
numeros2 = []

for i in range(1 , 6):
    numeros1.append(i)

for i in range(6 ,11 ):
    numeros2.append(i)    

productoEscolar =0
for i in range(len(numeros1)):
    productoEscolar += numeros1[i]*numeros2[2]

print("El peroducto escolar es: " , productoEscolar)