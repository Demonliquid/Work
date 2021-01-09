# %%
import os
import pandas as pd
import numpy as np
import datetime
from googletrans import Translator
from vininfo import Vin


# %%
motocarro = pd.read_excel(r'D:\Basededatos\Origen\MOTOCICLETAS-COLOMBIA\MOTOCARRO.xlsx', engine='openpyxl')


# %%
motocarro.rename(columns={'MODELO': 'AÑO', 'ORIGEN': 'IMPORTACION'}, inplace=True)
motocarro.drop_duplicates(inplace=True)
motocarroconvin = motocarro[motocarro["VIN"].str.len() == 17]
motocarroconvin = motocarroconvin[motocarroconvin["VIN"].str.contains('Q|O|I', regex=True) == False]
motocarrosinvin = pd.concat([motocarro, motocarroconvin, motocarroconvin]).drop_duplicates(keep=False)
motocarrosinvin["VIN"] = None
motocarrosinvin["ORIGEN"] = None



# %%
motocarroconvin["ORIGEN"] = motocarroconvin["VIN"].map(lambda x: Vin(x).country)
motocarroconvin['ORIGEN'].replace('China (Mainland)', 'China', inplace=True)
motocarroconvin['ORIGEN'].replace('Taiwan, China', 'China', inplace=True)
motocarroconvin['ORIGEN'].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
motocarroconvin['ORIGEN'].replace(r"Germany/West Germany", 'Alemania', inplace=True)
motocarroconvin['ORIGEN'].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
motocarroconvin['ORIGEN'].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
motocarroconvin['ORIGEN'].replace(r"United Kingdom", 'Reino Unido', inplace=True)
motocarroconvin['ORIGEN'].replace(r"Italy", 'Italia', inplace=True)
motocarroconvin['ORIGEN'].replace(r"Greece", 'Grecia', inplace=True)
motocarroconvin['ORIGEN'].replace(r"Belgium", 'Belgica', inplace=True)
motocarroconvin['ORIGEN'].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
motocarroconvin['ORIGEN'].replace(r"United States", 'Estados Unidos', inplace=True)
motocarroconvin['ORIGEN'].replace(r"Japan", 'Japon', inplace=True)
motocarroconvin['ORIGEN'].replace(r"Czech Republic", 'Republica Checa', inplace=True)
motocarroconvin['ORIGEN'].replace(r"United Arab Emirates", 'Emiratos Arabes Unidos', inplace=True)
motocarroconvin['ORIGEN'].replace(r"Ethiopia", 'Etiopía', inplace=True)


# %%
motocarro = pd.concat([motocarroconvin, motocarrosinvin])



# %%
dict(motocarro["ORIGEN"].value_counts())

# %%
motocarro.to_csv(r'D:\Basededatos\Limpioparaentregar\MOTOCICLETAS-COLOMBIA\motocarro.csv', index=False)


# %%