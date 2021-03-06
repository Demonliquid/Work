# %%
import os
import pandas as pd
import numpy as np
import datetime
from googletrans import Translator
from vininfo import Vin


# %%
motocicleta_p8 = pd.read_excel(r'D:\Basededatos\Origen\MOTOCICLETAS-COLOMBIA\MOTOCICLETA_P8.xlsx', engine='openpyxl')


# %%
motocicleta_p8.rename(columns={'MODELO': 'AÑO', 'ORIGEN': 'IMPORTACION'}, inplace=True)
motocicleta_p8.drop_duplicates(inplace=True)
motocicleta_p8convin = motocicleta_p8[motocicleta_p8["VIN"].str.len() == 17]
motocicleta_p8convin = motocicleta_p8convin[motocicleta_p8convin["VIN"].str.contains('Q|O|I', regex=True) == False]
motocicleta_p8sinvin = pd.concat([motocicleta_p8, motocicleta_p8convin, motocicleta_p8convin]).drop_duplicates(keep=False)
motocicleta_p8sinvin["VIN"] = None
motocicleta_p8sinvin["ORIGEN"] = None



# %%
motocicleta_p8convin["ORIGEN"] = motocicleta_p8convin["VIN"].map(lambda x: Vin(x).country)
motocicleta_p8convin['ORIGEN'].replace('China (Mainland)', 'China', inplace=True)
motocicleta_p8convin['ORIGEN'].replace('Taiwan, China', 'China', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Germany/West Germany", 'Alemania', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"United Kingdom", 'Reino Unido', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Italy", 'Italia', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Greece", 'Grecia', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Belgium", 'Belgica', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"United States", 'Estados Unidos', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Japan", 'Japon', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Czech Republic", 'Republica Checa', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"United Arab Emirates", 'Emiratos Arabes Unidos', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Ethiopia", 'Etiopia', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Hungary", 'Hungria', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Brazil", 'Brasil', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Spain", 'España', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"France", 'Francia', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Switzerland", 'Suiza', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Thailand", 'Tailandia', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Denmark", 'Dinamarca', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Finland", 'Finlandia', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Poland", 'Polonia', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Myanmar", 'Birmania', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Ireland", 'Irlanda', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Netherlands", 'Paises Bajos', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"South Africa", 'Sudafrica', inplace=True)
motocicleta_p8convin['ORIGEN'].replace(r"Morocco", 'Marruecos', inplace=True)


# %%
motocicleta_p8 = pd.concat([motocicleta_p8convin, motocicleta_p8sinvin])



# %%
dict(motocicleta_p8["ORIGEN"].value_counts())

# %%
motocicleta_p8.to_csv(r'D:\Basededatos\Limpioparaentregar\MOTOCICLETAS-COLOMBIA\motocicleta_p8.csv', index=False)


# %%