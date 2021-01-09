# %%
import os
import pandas as pd
import numpy as np
import datetime
from googletrans import Translator
from vininfo import Vin


# %%
ciclomotor = pd.read_excel(r'D:\Basededatos\Origen\MOTOCICLETAS-COLOMBIA\CICLOMOTOR.xlsx', engine='openpyxl')


# %%
ciclomotor.rename(columns={'MODELO': 'AÑO', 'ORIGEN': 'IMPORTACION'}, inplace=True)
ciclomotor["MARCA"].replace("STÿRKER", "STARKER", inplace=True)
ciclomotor.drop_duplicates(inplace=True)
ciclomotorconvin = ciclomotor[ciclomotor["VIN"].str.len() == 17]
ciclomotorconvin = ciclomotorconvin[ciclomotorconvin["VIN"].str.contains('Q|O|I', regex=True) == False]
ciclomotorsinvin = pd.concat([ciclomotor, ciclomotorconvin, ciclomotorconvin]).drop_duplicates(keep=False)
ciclomotorsinvin["VIN"] = None
ciclomotorsinvin["ORIGEN"] = None



# %%
ciclomotorconvin["ORIGEN"] = ciclomotorconvin["VIN"].map(lambda x: Vin(x).country)
ciclomotorconvin['ORIGEN'].replace('China (Mainland)', 'China', inplace=True)
ciclomotorconvin['ORIGEN'].replace('Taiwan, China', 'China', inplace=True)
ciclomotorconvin['ORIGEN'].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
ciclomotorconvin['ORIGEN'].replace(r"Germany/West Germany", 'Alemania', inplace=True)
ciclomotorconvin['ORIGEN'].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
ciclomotorconvin['ORIGEN'].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
ciclomotorconvin['ORIGEN'].replace(r"United Kingdom", 'Reino Unido', inplace=True)
ciclomotorconvin['ORIGEN'].replace(r"Italy", 'Italia', inplace=True)
ciclomotorconvin['ORIGEN'].replace(r"Greece", 'Grecia', inplace=True)
ciclomotorconvin['ORIGEN'].replace(r"Belgium", 'Belgica', inplace=True)
ciclomotorconvin['ORIGEN'].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
ciclomotorconvin['ORIGEN'].replace(r"United States", 'Estados Unidos', inplace=True)


# %%
ciclomotor = pd.concat([ciclomotorconvin, ciclomotorsinvin])



# %%
dict(ciclomotor["ORIGEN"].value_counts())

# %%
ciclomotor.to_csv(r'D:\Basededatos\Limpioparaentregar\MOTOCICLETAS-COLOMBIA\ciclomotor.csv', index=False)


# %%

# %%
