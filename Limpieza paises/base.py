# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DE DATOS

# MODELO
esquema = pd.read_excel(r'D:\Basededatos\Origen\Estructura_Base_Colombia-Dic20.xlsx', engine='openpyxl')


# %% BASE
esquema = esquema.iloc[0:0]


# %%
esquema.rename(columns={
                'TRACCION ': 'TRACCION'},
                inplace=True)


# %%
esquema.to_csv(r'D:\Basededatos\esquema.csv', index=False)


# %%