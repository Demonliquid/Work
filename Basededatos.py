# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DE DATOS

# MODELO
base = pd.read_csv(r'D:\Basededatos\esquema.csv')


# PAISES
colombia = pd.read_csv(r'D:\Basededatos\Limpioparaunir\colombia.csv')
chile = pd.read_csv(r'D:\Basededatos\Limpioparaunir\chile.csv')
paraguay = pd.read_csv(r'D:\Basededatos\Limpioparaunir\paraguay.csv')
guatemala = pd.read_csv(r'D:\Basededatos\Limpioparaunir\guatemala.csv')
costa_rica = pd.read_csv(r'D:\Basededatos\Limpioparaunir\costa_rica.csv')
elsalvador = pd.read_csv(r'D:\Basededatos\Limpioparaunir\elsalvador.csv')


# %% UNIR COLUMNAS IGUALES
base = pd.concat([
                 base,
                 colombia,
                 guatemala,
                 chile,
                 paraguay,
                 costa_rica,
                 elsalvador
                 ], join='outer')


# %%
base["GEN"] = base["GEN"].astype(str)
base["MOTOR"] = base["MOTOR"].astype(str)
base["CILINDRADA"] = base["CILINDRADA"].astype(str)
base["POTENCIA"] = base["POTENCIA"].astype(str)
base["CILINDROS.1"] = base["CILINDROS.1"].astype(str)
base["VALVULAS"] = base["VALVULAS"].astype(str)
base["AÑO"] = base["AÑO"].astype(str)


# %%
base.info()


# %%
base.to_csv(r'D:\Basededatos\Basededatos.csv', index=True)


# %%


