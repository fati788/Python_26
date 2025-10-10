### 9. Diccionario de estudiantes
#Crea un diccionario donde la clave sea el nombre de un estudiante y el valor su nota. Después:

#- Añade 3 estudiantes.
#- Muestra el promedio de las notas.
diccionario = {}
for i in range(3):
    clave = input("Dime el nombre: ")
    valor = float(input("Dime la nota: "))
    diccionario[clave] = valor

print(diccionario)

notas = diccionario.values()
print("La media es:", sum(notas)/len(notas))