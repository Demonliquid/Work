# %%
import os
import pandas as pd
import numpy as np
import datetime
from googletrans import Translator
from vininfo import Vin


# %%
cuadriciclo = pd.read_excel(r'D:\Basededatos\Origen\MOTOCICLETAS-COLOMBIA\CUADRICICLO.xlsx', engine='openpyxl')


# %%
cuadriciclo.rename(columns={'MODELO': 'AÑO', 'ORIGEN': 'IMPORTACION'}, inplace=True)
cuadriciclo.drop_duplicates(inplace=True)
cuadricicloconvin = cuadriciclo[cuadriciclo["VIN"].str.len() == 17]
cuadricicloconvin = cuadricicloconvin[cuadricicloconvin["VIN"].str.contains('Q|O|I', regex=True) == False]
cuadriciclosinvin = pd.concat([cuadriciclo, cuadricicloconvin, cuadricicloconvin]).drop_duplicates(keep=False)
cuadriciclosinvin["VIN"] = None
cuadriciclosinvin["ORIGEN"] = None



# %%
cuadricicloconvin["ORIGEN"] = cuadricicloconvin["VIN"].map(lambda x: Vin(x).country)
cuadricicloconvin['ORIGEN'].replace('China (Mainland)', 'China', inplace=True)
cuadricicloconvin['ORIGEN'].replace('Taiwan, China', 'China', inplace=True)
cuadricicloconvin['ORIGEN'].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
cuadricicloconvin['ORIGEN'].replace(r"Germany/West Germany", 'Alemania', inplace=True)
cuadricicloconvin['ORIGEN'].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
cuadricicloconvin['ORIGEN'].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
cuadricicloconvin['ORIGEN'].replace(r"United Kingdom", 'Reino Unido', inplace=True)
cuadricicloconvin['ORIGEN'].replace(r"Italy", 'Italia', inplace=True)
cuadricicloconvin['ORIGEN'].replace(r"Greece", 'Grecia', inplace=True)
cuadricicloconvin['ORIGEN'].replace(r"Belgium", 'Belgica', inplace=True)
cuadricicloconvin['ORIGEN'].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
cuadricicloconvin['ORIGEN'].replace(r"United States", 'Estados Unidos', inplace=True)


# %%
cuadriciclo = pd.concat([cuadricicloconvin, cuadriciclosinvin])



# %%
dict(cuadriciclo["ORIGEN"].value_counts())

# %%
cuadriciclo.to_csv(r'D:\Basededatos\Limpioparaentregar\MOTOCICLETAS-COLOMBIA\cuadriciclo.csv', index=False)


# %%