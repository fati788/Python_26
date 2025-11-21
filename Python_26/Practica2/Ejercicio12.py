
#Ejercicio 12: División segura

def division_segura(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    except ValueError:
        return "Error: Valores no numéricos proporcionados."
    except TypeError:
        return "Error: Tipos de datos incorrectos proporcionados."
# Ejemplo de uso
print(division_segura(10, 2))  # Salida: 5.0
print(division_segura(10, 0))  # Salida: Error: No se puede dividir por cero.
print(division_segura(10, 'a'))  # Salida: Error: Tipos de datos incorrectos proporcionados.
print(division_segura('x', 2))  # Salida: Error: Tipos de datos incorrectos proporcionados.
