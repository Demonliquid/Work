# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DE DATOS

# MODELO
base = pd.read_csv(r'D:\Basededatos\esquema.csv')


# %%
path = r'D:\Basededatos\Origen\Chile'
os.chdir(path)
files = os.listdir(path)
files


# %%
files_xls = [f for f in files if f[-4:] == 'xlsx']
files_xls

# %%
columnas = ['PPU', 'TIPO VEHICULO', 'MARCA', 'MODELO', 'AÑO FABRICACION']
chile = pd.DataFrame(columns=columnas)


# %%
for f in files_xls:
    data = pd.read_excel(f, engine='openpyxl')
    chile = pd.concat([chile , data], ignore_index=True, join='outer')


# %%
chile.duplicated().sum()


# %%
chile.drop_duplicates(inplace=True)


# %%
chile.info()


# %% DATOS LIMPIOS
chile.to_csv(r'D:\Basededatos\Limpioparaentregar\chile.csv', index=False)


# %%
chile = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\chile.csv')


# %% EQUIVALENCIA
chile["MERCADO"] = "CHILE"
chile["CANTIDAD"] = 1
chile.rename(columns={
                     'TIPO VEHICULO': 'SEGMENTO.1',
                     'AÑO FABRICACION': 'AÑO',
                     'PPU': 'PATENTE'},
                     inplace=True)


# %% FORMATO PARA UNIR
columnasutiles = [
                  "MERCADO",
                  "SEGMENTO.1",
                  "MARCA",
                  "MODELO",
                  "AÑO",
                  "PATENTE",
                  "CANTIDAD"]
chile = chile[columnasutiles]


# %%
chile["AÑO"].replace('nan', None, inplace=True)
chile["AÑO"].replace('NaN', None, inplace=True)

# %%
chile["AÑO"] = chile["AÑO"].astype("float").map('{:.0f}'.format)
chile["AÑO"] = chile["AÑO"].astype(int)
chile["AÑO"] = chile["AÑO"].astype(str)


# %%
chile.info()


# %%
chile.to_csv(r'D:\Basededatos\Limpioparaunir\chile.csv', index=False)


# %%
