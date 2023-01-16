import pandas as pd
import numpy as np
import pyodbc as dbc
import os
from dotenv import load_dotenv
load_dotenv()

# Declarar constantes
server = str(os.getenv('SERVER'))
bd = str(os.getenv('BD'))
usuario = str(os.getenv('USUARIO'))
contrasena = str(os.getenv('PASSWORD'))
query = '''
  SELECT 
		COUNT(peticion) as venta, MONTH([fecha_registro]) as mes, [documento_vendedor], DAY( fecha_registro) as dia, [zonal_vendedor], YEAR([fecha_registro]) as year,
  	CASE 
		WHEN DATEPART(WEEKDAY,fecha_registro) = 1 THEN 'lunes'
		WHEN DATEPART(WEEKDAY,fecha_registro) = 2 THEN 'martes'
		WHEN DATEPART(WEEKDAY,fecha_registro) = 3 THEN 'miercoles'
		WHEN DATEPART(WEEKDAY,fecha_registro) = 4 THEN 'jueves'
		WHEN DATEPART(WEEKDAY,fecha_registro) = 5 THEN 'viernes'
		WHEN DATEPART(WEEKDAY,fecha_registro) = 6 THEN 'sabado'
		WHEN DATEPART(WEEKDAY,fecha_registro) = 7 THEN 'domingo'
		ELSE 'DIA NO IDENTIFICADO'
	END AS DiaSemana
  FROM 
		[pbi].[dbo].[FJ_venta_registros] 
  WHERE 
		YEAR([fecha_registro])>=2022 AND [documento_vendedor] <> 'CTG000009'
  GROUP BY 
		[zonal_vendedor], [documento_vendedor], MONTH([fecha_registro]), DAY( fecha_registro), DATEPART(WEEKDAY,fecha_registro), YEAR([fecha_registro]) 
  ORDER BY 
		MONTH([fecha_registro]), DAY( fecha_registro), YEAR([fecha_registro]);
    '''


# Conectar con la base
def conectarBdDiario():
    try:
        conexion = dbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=' +
                               server+';DATABASE='+bd+';ENCRYPT=no;UID='+usuario+';PWD=' + contrasena)
        cursor = conexion.cursor()
        # query
        query_sql = query
        # Convertir a dataframe ventas
        consulta = pd.read_sql_query(query_sql, conexion)
        consulta['documento_vendedor'] = consulta['documento_vendedor'].astype(int)
        df_nuevo_index = consulta.set_index('documento_vendedor')
        df_final = df_nuevo_index.rename_axis('ID_VENTA')
        print("Conexión exitosa")
        return df_final

    except:
        print("Falló la conexión")


conectarBdDiario()
