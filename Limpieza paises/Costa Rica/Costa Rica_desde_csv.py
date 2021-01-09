# %%
import os
import pandas as pd
import numpy as np
import datetime
import xlrd


# %% CARGA DE DATOS

# MODELO
base = pd.read_csv(r'D:\Basededatos\esquema.csv')

# PAIS - ORIGINALES
costa_rica = pd.read_csv(r"D:\Basededatos\Limpioparaentregar\costa_rica_bruto.csv")


# %% 53201 filas
cambiarcilindroyposicion = costa_rica.loc[costa_rica["CILINDROS"].astype("str").str.isupper() == True]


# %%
costa_rica = costa_rica.drop(costa_rica[costa_rica["CILINDROS"].str.isalpha() == True].index)


# %%
cambiarcilindroyposicion.rename(columns={
                'CILINDROS': 'cilindros',
                'Posición Cilindros': 'CILINDROS',
                'cilindros': 'CILINDROS',
                },
                inplace=True)


# %% 
costa_rica = pd.concat([costa_rica, cambiarcilindroyposicion], join='outer')

# %%
costa_rica.to_csv(r'D:\Basededatos\Limpioparaentregar\costa_rica.csv', index=False)


# %%
costa_rica = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\costa_rica.csv')


# %% EQUIVALENCIAS
costa_rica["MERCADO"] = "COSTA RICA"
costa_rica["CANTIDAD"] = 1
costa_rica["TRANSMISION"].replace('M', 'MANUAL', inplace=True) 
costa_rica["TRANSMISION"].replace('A', 'AUTOMATICO', inplace=True) 
costa_rica["DISPOSICION CILINDROS"] = costa_rica["CILINDROS"].astype("str") + costa_rica["Posición Cilindros"].astype("str")



costa_rica.rename(columns={
                'MODELO': 'MODELOAREVISAR',
                'ESTILO': 'MODELO',
                'Número Motor': 'NUMERO MOTOR',
                'AÑO MODELO': 'AÑO',
                'CILINDRAJE': 'CILINDRADA',
                'TRACCION': 'TRACCION'
                },
                inplace=True)


# %% FORMATO PARA UNIR
columnasutiles = [
                  "MERCADO",
                  "MODELO",
                  "DISPOSICION CILINDROS",
                  "CILINDRADA",
                  "CILINDROS",
                  "NUMERO MOTOR",
                  "TRACCION",
                  "TRANSMISION",
                  "AÑO",
                  "CANTIDAD"]

costa_rica = costa_rica[columnasutiles]


# %%
costa_rica["CILINDRADA"].replace('nan', None, inplace=True)
costa_rica["CILINDRADA"].replace('NaN', None, inplace=True)

# %%
costa_rica["CILINDRADA"] = costa_rica["CILINDRADA"].astype("float").map('{:.0f}'.format)

# %%
costa_rica["AÑO"] = costa_rica["AÑO"].astype(int)
costa_rica["AÑO"] = costa_rica["AÑO"].astype(str)


# %%
costa_rica.to_csv(r'D:\Basededatos\Limpioparaunir\costa_rica.csv', index=False)


# %%
