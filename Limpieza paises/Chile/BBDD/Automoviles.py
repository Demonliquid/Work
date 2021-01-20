# %%
import os
import pandas as pd
import numpy as np
import datetime


# %%
BBDD500000 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVIES 500.000.csv')
BBDD1xls = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 1xls.csv')
BBDD1xlsx = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 1xlsx.csv')
BBDD2xls = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 2xls.csv')
BBDD2xlsx = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 2xlsx.csv')
BBDD3 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 3.csv')
BBDD4xls = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 4xls.csv')
BBDD4xlsx = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 4xlsx.csv')
BBDD5 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 5.csv')
BBDD6 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 6.csv')
BBDD7 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 7.csv')
BBDD8 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 8.csv')
BBDD9 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 9.csv')
BBDD10 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 10.csv')
BBDD11 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 11.csv')
BBDD12 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 12.csv')
BBDD13 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 13.csv')
BBDD14 = pd.read_csv(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\CSV\BBDD AUTOMÓVILES 14.csv')


# %%
BBDD1xls["RUT"] = BBDD1xls["RUT"].astype(str)+ "-" +BBDD1xls["DV"].astype(str)
BBDD2xls["RUT"] = BBDD2xls["RUT"].astype(str)+ "-" +BBDD2xls["DV"].astype(str)
BBDD2xlsx["RUT"] = BBDD2xlsx["RUT"].astype(str)+ "-" +BBDD2xlsx["DV"].astype(str)
BBDD3["RUT"] = BBDD3["RUT"].astype(str)+ "-" +BBDD3["DV"].astype(str)
BBDD4xls["RUT"] = BBDD4xls["RUT"].astype(str)+ "-" +BBDD4xls["DV"].astype(str)
BBDD4xlsx["RUT"] = BBDD4xlsx["RUT"].astype(str)+ "-" +BBDD4xlsx["DV"].astype(str)
BBDD6["RUT"] = BBDD6["RUT"].astype("float").map('{:.0f}'.format)
BBDD6["RUT"] = BBDD6["RUT"].astype(str)+ "-" +BBDD6["DV"].astype(str)
BBDD7["RUT"] = BBDD7["RUT"].astype("float").map('{:.0f}'.format)
BBDD7["RUT"] = BBDD7["RUT"].astype(str)+ "-" +BBDD7["DV"].astype(str)
BBDD9["RUT"] = BBDD9["RUT"].astype("float").map('{:.0f}'.format)
BBDD9["RUT"] = BBDD9["RUT"].astype(str)+ "-" +BBDD9["DV"].astype(str)
BBDD11["RUT"] = BBDD11["RUT"].astype("float").map('{:.0f}'.format)
BBDD11["RUT"] = BBDD11["RUT"].astype(str)+ "-" +BBDD11["DV"].astype(str)
BBDD12["RUT"] = BBDD12["RUT"].astype("float").map('{:.0f}'.format)
BBDD12["RUT"] = BBDD12["RUT"].astype(str)+ "-" +BBDD12["DV"].astype(str)
BBDD13["RUT"] = BBDD13["RUT"].astype("float").map('{:.0f}'.format)
BBDD13["RUT"] = BBDD13["RUT"].astype(str)+ "-" +BBDD13["DV"].astype(str)


# %% COLUMNAS UTILES
BBDD500000 = BBDD500000[['RUT', 'MARCA', 'MODELO', 'C.C', 'COMBUSTIBLE', 'PATENTE', 'CHARSIS', 'COMUNA']]
BBDD1xls = BBDD1xls[['RUT','comuna', 'Marca_VehIculo', 'Modelo', 'patente']]
BBDD1xlsx = BBDD1xlsx[['RUT CLIENTE','MARCA', 'MODELO', 'PATENTE', 'AÑO', 'CHARSIS']]
BBDD2xls = BBDD2xls[['RUT','comuna', 'Marca_VehIculo', 'Modelo', 'patente']]
BBDD2xlsx = BBDD2xlsx[['RUT','comuna', 'Marca_VehIculo', 'Modelo', 'patente']]
BBDD3 = BBDD3[['RUT','comuna', 'Marca_VehIculo', 'Modelo', 'patente']]
BBDD4xls = BBDD4xls[['RUT','comuna', 'Marca_VehIculo', 'Modelo', 'patente']]
BBDD4xlsx = BBDD4xlsx[['RUT','comuna', 'Marca_VehIculo', 'Modelo', 'patente']]
BBDD5 = BBDD5[['RUT_CLIENTE','MARCA', 'Modelo', 'patente']]
BBDD6 = BBDD6[['RUT','comuna', 'Marca_VehIculo', 'Modelo' ,'patente', 'CHARSIS']]
BBDD7 = BBDD7[['RUT','comuna', 'Marca_VehIculo', 'Modelo' ,'patente', 'CHARSIS']]
BBDD8 = BBDD8[['RUT CLIENTE','MARCA', 'MODELO', 'PATENTE', 'CHARSIS']]
BBDD9 = BBDD9[['RUT','COMUNA', 'MARCA', 'MODELO', 'PATENTE', 'CHARSIS']]
BBDD10 = BBDD10[['RUT CLIENTE','MARCA', 'MODELO', 'PATENTE', 'CHARSIS']]
BBDD11 = BBDD11[['RUT','COMUNA', 'MARCA', 'MODELO', 'PATENTE', 'CHARSIS']]
BBDD12 = BBDD12[['RUT','COMUNA', 'MARCA', 'MODELO', 'PATENTE', 'CHARSIS']]
BBDD13 = BBDD13[['RUT','COMUNA', 'MARCA', 'MODELO', 'PATENTE', 'CHARSIS']]
BBDD14 = BBDD14[['RUT','MARCA', 'MODELO', 'PATENTE', 'CHARSIS']]


# %% RENOMBRAR COLUMNAS
idx1 = {'CHARSIS': 'CHASIS'}
idx2 = {'Modelo': 'MODELO', 'patente': 'PATENTE'}
idx3 = {'CHARSIS': 'CHASIS', 'comuna': 'COMUNA', 'Marca_VehIculo': 'MARCA', 'Modelo':'MODELO', 'patente':'PATENTE' }

BBDD500000.rename(columns=idx1, inplace=True)
BBDD1xls.rename(columns=idx3, inplace=True)
BBDD1xlsx.rename(columns=idx1, inplace=True)
BBDD2xls.rename(columns=idx3, inplace=True)
BBDD2xlsx.rename(columns=idx3, inplace=True)
BBDD3.rename(columns=idx3, inplace=True)
BBDD4xls.rename(columns=idx3, inplace=True)
BBDD4xlsx.rename(columns=idx3, inplace=True)
BBDD5.rename(columns=idx2, inplace=True)
BBDD6.rename(columns=idx3, inplace=True)
BBDD7.rename(columns=idx3, inplace=True)
BBDD8.rename(columns=idx1, inplace=True)
BBDD9.rename(columns=idx1, inplace=True)
BBDD10.rename(columns=idx1, inplace=True)
BBDD11.rename(columns=idx1, inplace=True)
BBDD12.rename(columns=idx1, inplace=True)
BBDD13.rename(columns=idx1, inplace=True)
BBDD14.rename(columns=idx1, inplace=True)


# %%
idx1 = {'RUT CLIENTE' : 'RUT'}
idx2 = {'RUT_CLIENTE' : 'RUT'}

BBDD1xlsx.rename(columns=idx1, inplace=True)
BBDD5.rename(columns=idx2, inplace=True)
BBDD8.rename(columns=idx1, inplace=True)
BBDD10.rename(columns=idx1, inplace=True)


# %% 1669279
BBDD = pd.concat([BBDD500000,
                  BBDD1xls,
                  BBDD1xlsx,
                  BBDD2xls,
                  BBDD2xlsx,
                  BBDD3,
                  BBDD4xls,
                  BBDD4xlsx,
                  BBDD5,
                  BBDD7,
                  BBDD8,
                  BBDD9,
                  BBDD10,
                  BBDD11,
                  BBDD12,
                  BBDD13,
                  BBDD14
])
BBDD = BBDD[['RUT','MARCA', 'MODELO', 'C.C', 'COMBUSTIBLE', 'PATENTE', 'CHASIS', 'COMUNA']]


# %%
BBDD.drop_duplicates(inplace=True)
BBDD.dropna(inplace=True, how='all')

# %% 767811 
BBDD.info()
# %%
BBDD.to_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\BBDD.csv', index=False)


# %%
