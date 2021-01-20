# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% 5456993
definitiva = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES DEFINITIVA.csv')  # 888401
correctaydefinitiva = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES CORRECTA Y DEFINITIVA.csv')  # 888401
correctaycorrecta = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES CORRECTA Y CORRECTA.csv')  # 888401
completoycorrecto = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES COMPLETOS Y CORRECTOS.csv')  # 888401
completa200contactos1 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES COMPLETA 200.000 CONTACTOS 1.csv')  # 200000
completa200contactos2 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES COMPLETA 200.000 CONTACTOS 2.csv')  # 202450
milloncompleta200contactos1 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\MILLON BBDD AUTOMÓVILES COMPLETA 200.000 CONTACTOS 1.csv')  # 200000
milloncompleta200contactos2 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\MILLON BBDD AUTOMÓVILES COMPLETA 200.000 CONTACTOS 2.csv')  # 202450
milloncompleta200contactos3 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\MILLON BBDD AUTOMÓVILES COMPLETA 200.000 CONTACTOS 3.csv')  # 210088
milloncorrectaydefinitiva = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\MILLON BBDD AUTOMÓVILES CORRECTA Y DEFINITIVA.csv')  # 888401


# %%
completa200contactos1["RUT"] = completa200contactos1["RUT"].astype("float").map('{:.0f}'.format)
completa200contactos1["RUT"] = completa200contactos1["RUT"].astype(str)+ "-" +completa200contactos1["D. VERIFICADOR"].astype(str)
completa200contactos2["RUT"] = completa200contactos2["RUT"].astype("float").map('{:.0f}'.format)
completa200contactos2["RUT"] = completa200contactos2["RUT"].astype(str)+ "-" +completa200contactos2["D. VERIFICADOR"].astype(str)
milloncompleta200contactos1["RUT"] = milloncompleta200contactos1["RUT"].astype("float").map('{:.0f}'.format)
milloncompleta200contactos1["RUT"] = milloncompleta200contactos1["RUT"].astype(str)+ "-" +milloncompleta200contactos1["D. VERIFICADOR"].astype(str)
milloncompleta200contactos2["RUT"] = milloncompleta200contactos2["RUT"].astype("float").map('{:.0f}'.format)
milloncompleta200contactos2["RUT"] = milloncompleta200contactos2["RUT"].astype(str)+ "-" +milloncompleta200contactos2["D. VERIFICADOR"].astype(str)
milloncompleta200contactos3["RUT"] = milloncompleta200contactos3["RUT"].astype("float").map('{:.0f}'.format)
milloncompleta200contactos3["RUT"] = milloncompleta200contactos3["RUT"].astype(str)+ "-" +milloncompleta200contactos3["DV"].astype(str)




# %% COLUMNAS UTILES
definitiva = definitiva[['RUT', 'MARCA', 'MODELO', 'C.C', 'COMBUSTIBLE', 'PATENTE', 'CHASIS', 'COMUNA']]
correctaydefinitiva = correctaydefinitiva[['RUT', 'MARCA', 'MODELO', 'C.C', 'COMBUSTIBLE', 'PATENTE', 'CHARSIS', 'COMUNA']]
correctaycorrecta = correctaycorrecta[['RUT', 'MARCA', 'MODELO', 'C.C', 'COMBUSTIBLE', 'PATENTE', 'CHARSIS', 'COMUNA']]
completoycorrecto = completoycorrecto[['RUT', 'MARCA', 'MODELO', 'C.C', 'PATENTE', 'CHASIS', 'COMUNA']]
completa200contactos1 = completa200contactos1[['RUT','MARCA', 'MODELO', 'PATENTE', 'CHARSIS', 'COMUNA']]
completa200contactos2 = completa200contactos2[['RUT','MARCA', 'MODELO', 'PATENTE', 'CHARSIS', 'COMUNA']]
milloncompleta200contactos1 = milloncompleta200contactos1[['RUT','MARCA', 'MODELO', 'PATENTE', 'CHARSIS', 'COMUNA']]
milloncompleta200contactos2 = milloncompleta200contactos2[['RUT','MARCA', 'MODELO', 'PATENTE', 'CHARSIS', 'COMUNA']]
milloncompleta200contactos3 = milloncompleta200contactos3[['RUT','MARCA', 'MODELO', 'PATENTE', 'CHARSIS']]
milloncorrectaydefinitiva = milloncorrectaydefinitiva[['RUT', 'MARCA', 'MODELO', 'C.C', 'COMBUSTIBLE', 'PATENTE', 'CHARSIS', 'COMUNA']]


# %% RENOMBRAR COLUMNAS
idx = {'CHARSIS': 'CHASIS'}
correctaydefinitiva.rename(columns=idx, inplace=True)
correctaycorrecta.rename(columns=idx, inplace=True)
completa200contactos1.rename(columns=idx, inplace=True)
completa200contactos2.rename(columns=idx, inplace=True)
milloncompleta200contactos1.rename(columns=idx, inplace=True)
milloncompleta200contactos2.rename(columns=idx, inplace=True)
milloncompleta200contactos3.rename(columns=idx, inplace=True)
milloncorrectaydefinitiva.rename(columns=idx, inplace=True)


# %% 5456993
labuena = pd.concat([definitiva,
                     correctaydefinitiva,
                     correctaycorrecta,
                     completoycorrecto,
                     completa200contactos1,
                     completa200contactos2,
                     milloncompleta200contactos1,
                     milloncompleta200contactos2,
                     milloncompleta200contactos3,
                     milloncorrectaydefinitiva])


# %% ELIMINAR SOBRANTE
labuena.drop_duplicates(inplace=True)
labuena.dropna(inplace=True, how='all')


# %% 1096638
labuena.info()


# %%
labuena.to_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\Definitiva.csv')

# %%
