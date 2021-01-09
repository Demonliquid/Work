# %%
import os
import pandas as pd
import numpy as np
import datetime

# %% CARGA DE DATOS

# MODELO
base = pd.read_csv(r'D:\Basededatos\esquema.csv')

# PAIS
colombia = pd.read_excel(r'D:\Basededatos\Origen\Estructura_Base_Colombia-Dic20.xlsx', engine='openpyxl')


# %% EQUIVALENCIA COLOMBIA-BASE
colombia.rename(columns={
                'TRACCION ': 'TRACCION'},
                inplace=True)


# %% DATOS LIMPIOS
colombia.to_csv(r'D:\Basededatos\Limpioparaentregar\colombia.csv', index=False)


# %%
colombia.to_csv(r'D:\Basededatos\Limpioparaunir\colombia.csv', index=False)
# %%
dict(colombia["GEN"].value_counts())
# %%
