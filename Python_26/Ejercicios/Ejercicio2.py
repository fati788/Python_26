### 2. Clasificación de edad

edad = int(input("Introduce tu edad: "))

if edad <18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
elif edad >= 65:
    print("Eres adulto mayor.") 
else:
    print("Edad no válida.")


    