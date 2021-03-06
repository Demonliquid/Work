# %%
import os
import pandas as pd
import numpy as np
import datetime
from googletrans import Translator
from vininfo import Vin


# %%
motocicleta_p2 = pd.read_excel(r'D:\Basededatos\Origen\MOTOCICLETAS-COLOMBIA\MOTOCICLETA_P2.xlsx', engine='openpyxl')


# %%
motocicleta_p2.rename(columns={'MODELO': 'AÑO', 'ORIGEN': 'IMPORTACION'}, inplace=True)
motocicleta_p2.drop_duplicates(inplace=True)
motocicleta_p2convin = motocicleta_p2[motocicleta_p2["VIN"].str.len() == 17]
motocicleta_p2convin = motocicleta_p2convin[motocicleta_p2convin["VIN"].str.contains('Q|O|I', regex=True) == False]
motocicleta_p2sinvin = pd.concat([motocicleta_p2, motocicleta_p2convin, motocicleta_p2convin]).drop_duplicates(keep=False)
motocicleta_p2sinvin["VIN"] = None
motocicleta_p2sinvin["ORIGEN"] = None



# %%
motocicleta_p2convin["ORIGEN"] = motocicleta_p2convin["VIN"].map(lambda x: Vin(x).country)
motocicleta_p2convin['ORIGEN'].replace('China (Mainland)', 'China', inplace=True)
motocicleta_p2convin['ORIGEN'].replace('Taiwan, China', 'China', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Germany/West Germany", 'Alemania', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"United Kingdom", 'Reino Unido', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Italy", 'Italia', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Greece", 'Grecia', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Belgium", 'Belgica', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"United States", 'Estados Unidos', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Japan", 'Japon', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Czech Republic", 'Republica Checa', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"United Arab Emirates", 'Emiratos Arabes Unidos', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Ethiopia", 'Etiopia', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Hungary", 'Hungria', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Brazil", 'Brasil', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Spain", 'España', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"France", 'Francia', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Switzerland", 'Suiza', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Thailand", 'Tailandia', inplace=True)
motocicleta_p2convin['ORIGEN'].replace(r"Denmark", 'Dinamarca', inplace=True)




# %%
motocicleta_p2 = pd.concat([motocicleta_p2convin, motocicleta_p2sinvin])



# %%
dict(motocicleta_p2["ORIGEN"].value_counts())

# %%
motocicleta_p2.to_csv(r'D:\Basededatos\Limpioparaentregar\MOTOCICLETAS-COLOMBIA\motocicleta_p2.csv', index=False)


# %%