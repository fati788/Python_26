num1 = int(input("Dame un numero: "))
num2 = int(input("Dame otro numero: "))

if num1 > num2:
    num1 , num2 = num2, num1
for i in range(num1 , num2+1):
    if i%2 == 0 : 
        print(i)
#compresion de listas
pares = [i for i in range(num1 , num2+1)  if i%2 == 0 ] 
print(pares)       