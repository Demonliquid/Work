# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DE DATOS

path = r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD 9 MILLONES PATENTES Y CHASIS'
os.chdir(path)
files = os.listdir(path)
files


# %%
files_xls = [f for f in files if f[-4:] == 'xlsx']
files_xls

# %%
columnas = ['PATENTE', 'CHASIS']
patentesychasis = pd.DataFrame(columns=columnas)


# %% 8882192
for f in files_xls:
    data = pd.read_excel(f, engine='openpyxl')
    patentesychasis = pd.concat([patentesychasis , data], ignore_index=True, join='outer')

# %%
patentesychasis2 = patentesychasis.drop_duplicates(subset=["PATENTE"])


# %%
patentesychasis2.rename(columns={"CHASIS": "NUMERO CHASIS / VIN"}, inplace=True)


# %%
patentesychasis2.to_csv(r'D:\Basededatos\Limpioparaunir\patentesychasis.csv', index=False)

# %%
