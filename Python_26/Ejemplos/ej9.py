diccionario = {}
for i in range(3):
    clave = input("Introduce el nombre del estudiante: ")
    valor = float(input("Introduce la nota del estudiante: "))
    diccionario[clave] = valor 

print(diccionario)    

notas = diccionario.values()
print("el medio: " , sum(notas)/len(notas))