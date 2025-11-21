"""
Ejercicio 5: Gestor de fechas

Usa el módulo datetime para crear una función que:

    Reciba una fecha de cumpleaños (día, mes, año)
    Calcule cuántos días faltan para el próximo cumpleaños
    Si ya pasó este año, calcule para el próximo año

"""
from datetime import datetime
def dias_para_cumpleanos(dia, mes, anio):
    hoy = datetime.now()
    cumpleanos_este_ano = datetime(hoy.year, mes, dia)

    if cumpleanos_este_ano < hoy:
        cumpleanos_proximo = datetime(hoy.year + 1, mes, dia)
    else:
        cumpleanos_proximo = cumpleanos_este_ano

    dias_faltantes = (cumpleanos_proximo - hoy).days
    return dias_faltantes
# Ejemplo de uso
dia = 1
mes = 8
anio = 2005
faltan_dias = dias_para_cumpleanos(dia, mes, anio)
print(f"Días para el próximo cumpleaños: {faltan_dias}")
