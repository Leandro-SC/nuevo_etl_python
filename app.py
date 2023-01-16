from models import Class_BD as bd
from models import Class_Sheets as bd_sheets
from models import Compartir_Sheets as sheet
from models import Class_Operaciones as op
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date

def main():

    #Instancias 
    base_ffvv = bd_sheets.ConectarGoogleSheets()
    base_ventas = bd.conectarBdDiario()
    # ventas = base_ventas.where((base_ventas.mes == 1) )
    print(type(base_ventas))


    #ingresar proy. lineal

    #agregar status
    

    #Unificar tablas
    df_general = base_ffvv.merge(ventas, left_on='ID_VENTA', right_on='ID_VENTA', how='outer')
    df_general.fillna(0, inplace=True)
    df_ventas = df_general.where((df_general.Nombre_Completo != 0))
    
    #Generar Tabla pivote
    tabla_resumen = df_ventas.pivot_table(
        index=['Nombre_Completo','Zonal','Supervisor','Fecha_Ingreso','Estado_Vendedor','Tipo_Esquema'], 
        columns=['dia'],values= 'venta',
        aggfunc=sum,fill_value=0).sort_values(by=['Zonal','Supervisor'])

    #Agregar columnas calculadas
    tabla = pd.DataFrame(tabla_resumen)
    nueva_tabla = tabla.drop(tabla.columns[0], axis=1)
    #Agregar Dias
    columna_fecha = nueva_tabla.index.values
    list_nueva = op.formatearFecha(columna_fecha)
    list_dias = []
    for x in list_nueva:
        valor = op.calcularDiasPermanencia(x)
        result = valor / 30
        list_dias.append(result)
    nueva_tabla['Meses']= list_dias
    # nueva_tabla['Dias_Permanencia'] =  op.calcularDiasPermanencia(fecha)
    nueva_tabla['Prom_Rus']= nueva_tabla.drop(["Meses"],axis=1).mean(axis=1)
    nueva_tabla['Total_Rus']=  nueva_tabla.drop(["Prom_Rus","Meses"],axis=1).sum(axis=1)
    
    #Generar Excel
    # tabla_excel = nueva_tabla.to_excel('mapa_calor_fija.xlsx',sheet_name="ventas_dia")

    # print(nueva_tabla)

    
    
   
main()




















