import pandas as pd
import numpy as np
from datetime import date, timedelta, datetime
import calendar
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR, SA, SU


def calcularDiasPermanencia(fechaIngreso):

    fecha_actual = date.today().strftime("%d/%m/%Y")
    formato = "%d/%m/%Y"
    fecha_hoy = datetime.strptime(fecha_actual, formato)
    fecha_ingreso = datetime.strptime(fechaIngreso, formato)
    diferencia = fecha_hoy - fecha_ingreso

    return diferencia.days


def formatearFecha(valor):
    lista_fecha = []
    for i in valor:
        lista_fecha.append(i[3])
    return lista_fecha


def agregarValoresColumna():
    pass


def asignarCuotaRU(meses):
    cuota = 0
    if meses >= 3:
        cuota = 24
    elif meses >= 2:
        cuota = 12
    else:
        cuota = 6
    return cuota


def asignarCuotaAltas(meses):
    cuota = 0
    if meses >= 3:
        cuota = 12
    elif meses >= 2:
        cuota = 6
    else:
        cuota = 3
    return cuota


def asignarClusterProductividad(ventas):
    cluster = ''
    if ventas >= 26:
        cluster = 'MUY BUENO'
    elif ventas >= 20:
        cluster = 'BUENO'
    elif ventas >= 10:
        cluster = 'REGULAR'
    elif ventas >= 5:
        cluster = 'CRITICO'
    else:
        cluster = 'MUY CRITICO'
    return cluster

def calcularObjetivoDiario(diasMes, diasVenta, cuota, ventas):

    try:
        obj = (cuota-ventas) / (diasMes-diasVenta)
    except:
        obj = 1
    return obj


def statusDiasVenta(valor):
    status = ''
    if valor > 2:
        status = 'CRITICO'
    elif valor > 1:
        status = 'REGULAR'
    else:
        status = 'BUENO'

    return status

# Calcular dias de un mes
def obtener_dias_del_mes(mes: int):
    # Abril, junio, septiembre y noviembre tienen 30
    if mes in [4, 6, 9, 11]:
        return 30
    # Febrero depende de si es o no bisiesto
    if mes == 2:
        return 28
    else:
        # En caso contrario, tiene 31 días
        return 31

def contarDomingo():
    year = date.today().year
    mes = date.today().month
    dia = datetime.today().weekday() #igualar a 6
    # dia_inicio =  datetime(year,mes,1)
    # ultimo_dia = datetime(year,mes,last_day)
    last_day = calendar.monthrange (year, mes) [1]
    first_day = calendar.monthrange (year, mes)[0]
    start_date = date(year, mes, 1)
    end_date = date(year, mes, last_day)

    sunday_count = len(list(rrule(DAILY, byweekday=(SU), dtstart=start_date, until=end_date)))
    return sunday_count

def calcularProyeccion(ventas):
    dias_domingos  = contarDomingo()
    mes2 = obtener_dias_del_mes(date.today().month) - dias_domingos
    mes1 = int(date.today().strftime("%d"))
    
    diasMes = mes2 - mes1
    proy = ventas*mes2/diasMes
    return round(proy, 2)

valor = calcularProyeccion(30)
print(valor)
