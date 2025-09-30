### 9. Diccionario de estudiantes
#Crea un diccionario donde la clave sea el nombre de un estudiante y el valor su nota. Después:

#- Añade 3 estudiantes.
#- Muestra el promedio de las notas.
estudiantes = {}
for i in range(3):
    nombre = input("Introduce el nombre del estudiante: ")
    nota = float(input("Introduce la nota del estudiante: "))
    estudiantes[nombre] = nota  
promedio = sum(estudiantes.values()) / len(estudiantes)
print("El promedio de las notas es:", promedio)