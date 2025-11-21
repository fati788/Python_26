
#Ejercicio 13: Conversión robusta

def convertir_a_enteros(lista_strings):
    numeros_convertidos = []
    errores = []
    for i in lista_strings:
        try:
            numero = int(i)
            numeros_convertidos.append(numero)
        except ValueError:
            errores.append(f"{i} no se pudo convertir")
    return numeros_convertidos, errores
# Ejemplo de uso
datos = ["10", "20", "abc", "30", "xyz", "40"]
resultado = convertir_a_enteros(datos)  
print(resultado)
