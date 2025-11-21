"""
Ejercicio 2: Validador de contraseñas

Escribe una función que valide si una contraseña cumple los siguientes criterios:

    Al menos 8 caracteres
    Al menos una letra mayúscula
    Al menos una letra minúscula
    Al menos un número
    Al menos un carácter especial (@, #, $, %, etc.)

La función debe retornar True si cumple todos los criterios, False en caso contrario.
"""
# Función para validar contraseñas
def validar_contrasena(contrasena):
    import re

    if len(contrasena) < 8:
        return False
    if not re.search(r'[A-Z]', contrasena):
        return False
    if not re.search(r'[a-z]', contrasena):
        return False
    if not re.search(r'[0-9]', contrasena):
        return False
    if not re.search(r'[@#$%&*!]', contrasena):
        return False

    return True
# Ejemplo de uso
contrasena = "Password123!"
print(validar_contrasena(contrasena))  # Salida: True    
contrasena_invalida = "pass"
print(validar_contrasena(contrasena_invalida))  # Salida: False