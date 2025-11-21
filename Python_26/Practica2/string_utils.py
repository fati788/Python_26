"""
Ejercicio 4: Utilidades de strings

Crea un módulo string_utils.py con las siguientes funciones:

    invertir_texto(texto): Invierte el orden de los caracteres
    contar_vocales(texto): Cuenta cuántas vocales hay
    es_palindromo(texto): Verifica si es un palíndromo
    capitalizar_palabras(texto): Capitaliza la primera letra de cada palabra

Importa y usa estas funciones en otro archivo.
"""
# string_utils.py
# invertir_texto(texto): Invierte el orden de los caracteres
def invertir_texto(texto):
    return texto[::-1]
# contar_vocales(texto): Cuenta cuántas vocales hay
def contar_vocales(texto):
    vocales = 'aeiouAEIOU'
    cotador = 0
    for char in texto:
        if char in vocales:
            cotador += 1
    return cotador
# es_palindromo(texto): Verifica si es un palíndromo
def es_palindromo(texto):
    textto =""
    for char in texto:
        if char.isalnum():  # Ignorar espacios y puntuación
            textto += char.lower()  # Convertir a minúsculas
    return textto == textto[::-1]
# capitalizar_palabras(texto): Capitaliza la primera letra de cada palabra
def capitalizar_palabras(texto):
    return texto.title()
