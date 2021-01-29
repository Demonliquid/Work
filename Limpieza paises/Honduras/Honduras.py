# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DE DATOS
path = r'D:\Basededatos\Origen\Honduras'
os.chdir(path)
files = os.listdir(path)
files

files_xls = [f for f in files if f[-4:] == 'xlsx']
files_xls

# %%

honduras = pd.DataFrame()


for f in files_xls:
    data = pd.read_excel(f, engine='openpyxl')
    honduras = pd.concat([honduras , data], ignore_index=True, join='outer')


# %%
honduras = honduras[["AÑO DEL VEHICULO", "TIPO", "TIPO DE\nCOMBUSTIBLE", "MARCA", "MODELO", "CILINDRAJE", "CANTIDAD DE\nPLACAS"]]


# %%
honduras["MERCADO"] = "HONDURAS"
honduras.rename(columns={"TIPO DE\nCOMBUSTIBLE": "TIPO DE COMBUSTIBLE", "CANTIDAD DE\nPLACAS": "CANTIDAD DE PLACAS", "MODELO":"MODELO/VERSION"}, inplace=True)



# %%
honduras.to_csv(r'D:\Basededatos\Limpioparaunir\honduras.csv', index=False)
