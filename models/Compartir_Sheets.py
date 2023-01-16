import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

scope = ['https://www.googleapis.com/auth/spreadsheets',
        "https://www.googleapis.com/auth/drive"]

credenciales = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
cliente = gspread.authorize(credenciales)

# sheet = cliente.create("Mapa de Calor AG")
# sheet.share('leandrosilva.auren@gmail.com', perm_type='user', role='writer', notify=True)
def actualizarHoja(archivoExcel):

    libro_lectura = cliente.open_by_key("1C4fkxWrXavRs6Vx0l5ejbOeXPy3k-98ssQbufUDVCHw").sheet1
    df = pd.read_excel(archivoExcel)
    datos_columnas = df.columns.values.tolist()
    datos_valores = df.values.tolist()
    return libro_lectura.update([datos_columnas] + datos_valores)
