cadena = "hola mundo"
lista = [letra for letra in cadena if letra in "aeuio" ]
print(lista)

numbers = [(i, i * i) for i in range(11)]
print(numbers)    
#pares del 0 al 40 
even_numbers = [i for i in range(40) if i % 2 == 0] 
print(even_numbers) 