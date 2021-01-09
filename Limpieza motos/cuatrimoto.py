# %%
import os
import pandas as pd
import numpy as np
import datetime
from googletrans import Translator
from vininfo import Vin


# %%
cuatrimoto = pd.read_excel(r'D:\Basededatos\Origen\MOTOCICLETAS-COLOMBIA\CUATRIMOTO.xlsx', engine='openpyxl')


# %%
cuatrimoto.rename(columns={'MODELO': 'AÑO', 'ORIGEN': 'IMPORTACION'}, inplace=True)
cuatrimoto.drop_duplicates(inplace=True)
cuatrimotoconvin = cuatrimoto[cuatrimoto["VIN"].str.len() == 17]
cuatrimotoconvin = cuatrimotoconvin[cuatrimotoconvin["VIN"].str.contains('Q|O|I', regex=True) == False]
cuatrimotosinvin = pd.concat([cuatrimoto, cuatrimotoconvin, cuatrimotoconvin]).drop_duplicates(keep=False)
cuatrimotosinvin["VIN"] = None
cuatrimotosinvin["ORIGEN"] = None



# %%
cuatrimotoconvin["ORIGEN"] = cuatrimotoconvin["VIN"].map(lambda x: Vin(x).country)
cuatrimotoconvin['ORIGEN'].replace('China (Mainland)', 'China', inplace=True)
cuatrimotoconvin['ORIGEN'].replace('Taiwan, China', 'China', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"Germany/West Germany", 'Alemania', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"United Kingdom", 'Reino Unido', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"Italy", 'Italia', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"Greece", 'Grecia', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"Belgium", 'Belgica', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"United States", 'Estados Unidos', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"Japan", 'Japon', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"Czech Republic", 'Republica Checa', inplace=True)
cuatrimotoconvin['ORIGEN'].replace(r"United Arab Emirates", 'Emiratos Arabes Unidos', inplace=True)


# %%
cuatrimoto = pd.concat([cuatrimotoconvin, cuatrimotosinvin])



# %%
dict(cuatrimoto["ORIGEN"].value_counts())

# %%
cuatrimoto.to_csv(r'D:\Basededatos\Limpioparaentregar\MOTOCICLETAS-COLOMBIA\cuatrimoto.csv', index=False)


# %%