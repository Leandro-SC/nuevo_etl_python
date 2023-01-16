import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os
from datetime import date

scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credenciales = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
cliente = gspread.authorize(credenciales)
sheets_key = "1C4fkxWrXavRs6Vx0l5ejbOeXPy3k-98ssQbufUDVCHw"

def ConectarGoogleSheets():

    libro_lectura = cliente.open_by_key(sheets_key)
    # Informacion FFVV
    hoja_lectura = libro_lectura.worksheet('BASE')
    datos = hoja_lectura.get_all_values()[1:]
    df_ffvv = pd.DataFrame(datos)
    df_ffvv.rename(columns={
        0: 'Canal', 1: 'Zonal', 2: 'Tipo_Doc.', 3: 'Numero_Doc',
        4: 'Nombre_Completo', 5: 'Supervisor', 6: 'Fecha_Ingreso', 7: 'Estado_Vendedor',
        8: 'Fecha_Cese', 9: 'Tipo_Esquema', 10:'ID_VENTA', 11:"Codigo_Auditor"},
        inplace=True)
    df_ffvv['ID_VENTA'] = df_ffvv['ID_VENTA'].astype(int)
    df_nuevo_index = df_ffvv.set_index('ID_VENTA')
    # print(df_nuevo_index)
    return df_nuevo_index


def conectarCuotasSheets():
    pass


# ConectarGoogleSheets()



