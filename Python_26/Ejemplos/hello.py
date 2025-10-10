#Esto es mi primer programa en Python
print("Hola mundo")

print("otra cosa")

print(type(3.5))
print(type([1,2,3]))

numero = 100
cadena = "Hola mundo"
booleano = True
#es 3.4 x 10^10
floatExponencial = 3.4e10

print(numero)
print(cadena)
print(booleano)
print(floatExponencial)


print(type(numero))
print(type(cadena))
print(type(booleano))

#el tipo de dato de una variable puede cambiar
numero = "Ahora soy una cadena"
print(numero)
print(type(numero))

numero, contador, acumulador = 10,20,30
print(numero, contador, acumulador)


print(reversed("Hola mundo"))

#longitud de una cadena
print(len("Hola mundo"))

nombre = input("Dime tu nombre: ")
print("Hola ", nombre)
edad = input("Dime tu edad: ")
print("Tienes " , edad , " años")
print(type(edad))
edad = int(edad) 

#leemos un numero y lo convertimos a float
precio = float(input("Dime el precio: "))
print("El precio es: ", precio)
print(type(precio))