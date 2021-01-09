# %%
import os
import pandas as pd
import numpy as np
import datetime
from googletrans import Translator
from vininfo import Vin


# %%
mototriciclo = pd.read_excel(r'D:\Basededatos\Origen\MOTOCICLETAS-COLOMBIA\MOTOTRICICLO.xlsx', engine='openpyxl')


# %%
mototriciclo.rename(columns={'MODELO': 'AÑO', 'ORIGEN': 'IMPORTACION'}, inplace=True)
mototriciclo.drop_duplicates(inplace=True)
mototricicloconvin = mototriciclo[mototriciclo["VIN"].str.len() == 17]
mototricicloconvin = mototricicloconvin[mototricicloconvin["VIN"].str.contains('Q|O|I', regex=True) == False]
mototriciclosinvin = pd.concat([mototriciclo, mototricicloconvin, mototricicloconvin]).drop_duplicates(keep=False)
mototriciclosinvin["VIN"] = None
mototriciclosinvin["ORIGEN"] = None



# %%
mototricicloconvin["ORIGEN"] = mototricicloconvin["VIN"].map(lambda x: Vin(x).country)
mototricicloconvin['ORIGEN'].replace('China (Mainland)', 'China', inplace=True)
mototricicloconvin['ORIGEN'].replace('Taiwan, China', 'China', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Germany/West Germany", 'Alemania', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"United Kingdom", 'Reino Unido', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Italy", 'Italia', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Greece", 'Grecia', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Belgium", 'Belgica', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"United States", 'Estados Unidos', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Japan", 'Japon', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Czech Republic", 'Republica Checa', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"United Arab Emirates", 'Emiratos Arabes Unidos', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Ethiopia", 'Etiopia', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Hungary", 'Hungria', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Brazil", 'Brasil', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Spain", 'España', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"France", 'Francia', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Switzerland", 'Suiza', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Thailand", 'Tailandia', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Denmark", 'Dinamarca', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Finland", 'Finlandia', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Poland", 'Polonia', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Myanmar", 'Birmania', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Ireland", 'Irlanda', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Netherlands", 'Paises Bajos', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"South Africa", 'Sudafrica', inplace=True)
mototricicloconvin['ORIGEN'].replace(r"Morocco", 'Marruecos', inplace=True)


# %%
mototriciclo = pd.concat([mototricicloconvin, mototriciclosinvin])



# %%
dict(mototriciclo["ORIGEN"].value_counts())

# %%
mototriciclo.to_csv(r'D:\Basededatos\Limpioparaentregar\MOTOCICLETAS-COLOMBIA\mototriciclo.csv', index=False)


# %%