#18. Combinación de diccionarios
diccionario1 = {
    "edad":18,
    "vida": 100,
    "numero":30
}
diccionario2={
"edad":18,
"vida": 100,
"algo":40
}
diccionario3 = diccionario1.copy()

for  clave, valor in diccionario2.items():
    if clave in diccionario3:
        diccionario3[clave] += valor
    else:
         diccionario3[clave] = valor
print("Diccionario 1:" , diccionario1)            
print("Diccionario 2:" , diccionario2)
print("Diccionario 3:" , diccionario3)