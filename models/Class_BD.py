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
AGREGAR QUERY
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
