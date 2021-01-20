# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DE DATOS 195106
RSA = pd.read_excel(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD AUTOMÓVILES SEGUROS RSA.xlsx', engine='openpyxl')  # 77591
MAGALLANES = pd.read_excel(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD AUTOMÓVILES SEGUROS MAGALLANES.xls')  # 13024
PENTA = pd.read_excel(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD AUTOMÓVILES PENTA SECURITY.xls')  # 13248
LIBERTY = pd.read_excel(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD AUTOMÓVILES LIBERTY SECURITY.xlsx', engine='openpyxl')  # 77591
BCI1 = pd.read_excel(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD AUTOMÓVILES BCI SEGUROS.xls')  # 13248
BCI2 =  pd.read_excel(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD AUTOMÓVILES BCI SEGUROS 2.xlsx', engine='openpyxl')  # 404


# %%
MAGALLANES["RUT"] = MAGALLANES["RUT"].astype("float").map('{:.0f}'.format)
MAGALLANES["RUT"] = MAGALLANES["RUT"].astype(str)+ "-" +MAGALLANES["DV"].astype(str)
PENTA["RUT"] = PENTA["RUT"].astype("float").map('{:.0f}'.format)
PENTA["RUT"] = PENTA["RUT"].astype(str)+ "-" +PENTA["DV"].astype(str)
BCI1["RUT"] = BCI1["RUT"].astype("float").map('{:.0f}'.format)
BCI1["RUT"] = BCI1["RUT"].astype(str)+ "-" +BCI1["DV"].astype(str)
BCI2["RUT"] = BCI2["RUT"].astype("float").map('{:.0f}'.format)
BCI2["RUT"] = BCI2["RUT"].astype(str)+ "-" +BCI2["DV"].astype(str)


# %% COLUMNAS UTILES
RSA = RSA[["RUT_CLIENTE",'MARCA', 'Modelo', 'patente']]
MAGALLANES = MAGALLANES[["RUT",'comuna', 'Marca_VehIculo', 'Modelo', 'patente']]
PENTA = PENTA[["RUT",'comuna', 'Marca_VehIculo', 'Modelo', 'patente']]
LIBERTY = LIBERTY[['RUT_CLIENTE','MARCA', 'Modelo', 'patente']]
BCI1 = BCI1[['RUT','comuna', 'Marca_VehIculo', 'Modelo', 'patente']]
BCI2 = BCI2[['RUT','comuna', 'Marca_VehIculo', 'Modelo', 'patente']]


# %% RENOMBRAR
idx = {'Marca_VehIculo': 'MARCA'}
idx2 = {'RUT_CLIENTE': "RUT"}
MAGALLANES.rename(columns=idx, inplace=True)
PENTA.rename(columns=idx, inplace=True)
BCI1.rename(columns=idx, inplace=True)
BCI2.rename(columns=idx, inplace=True)
RSA.rename(columns=idx2, inplace=True)
LIBERTY.rename(columns=idx2, inplace=True)


# %% 195106
seguros = pd.concat([RSA, MAGALLANES, PENTA, LIBERTY, BCI1, BCI2])

# %% 90429
seguros.drop_duplicates(inplace=True)
seguros.dropna(inplace=True, how='all')

#%%
seguros.info()

# %%
seguros.to_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\seguros.csv')
# %%
