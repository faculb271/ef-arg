import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_file(r"C:\Users\Facundo\Documents\Python proyectos\key.json", scopes=SCOPES)

gc = gspread.authorize(creds)
# Verifica la conexión listando tus hojas de cálculo
sheets = gc.openall()

# Abrir la hoja de cálculo y la pestaña "Main"
spreadsheet = gc.open("OPC_Main")
hoja = spreadsheet.worksheet("Main")

# Leer datos hasta la fila 105
datos = hoja.get_all_values()
df = pd.DataFrame(datos[3:], columns=datos[2])

print(df)