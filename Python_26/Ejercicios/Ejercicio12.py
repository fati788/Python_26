### 12. Número primo

#Escribe un programa que determine si un número ingresado por el usuario es primo o no.

numero = int(input("Dame un numero: "))
primo = True
for  i in range(2, numero ):
  if numero % i == 0:
    primo = False


if primo:
  print("El numero es primo")
else:
  print("El numero NOOO es primo")    
