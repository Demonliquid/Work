# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DATOS 217065
MB1 = pd.read_excel(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD AUTOMÓVILES MERCEDES BENZ Y B.M.W. 1.xlsx', engine='openpyxl')  # 99955
MB2 = pd.read_excel(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD AUTOMÓVILES MERCEDES BENZ Y B.M.W. 2.xlsx', engine='openpyxl')  # 13024
MB3 = pd.read_excel(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD AUTOMÓVILES MERCEDES BENZ Y B.M.W. 3.xlsx', engine='openpyxl')  # 13248
MB4 = pd.read_excel(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD AUTOMÓVILES MERCEDES BENZ Y B.M.W. 4.xlsx', engine='openpyxl')  # 13248
MB5 = pd.read_excel(r'D:\Basededatos\Origen\BBDD AUTOMÓVILES 9 MILLONES\BBDD AUTOMÓVILES MERCEDES BENZ Y B.M.W. 5.xlsx', engine='openpyxl')  # 77590


# %%
MB2["RUT"] = MB2["RUT"].astype("float").map('{:.0f}'.format)
MB2["RUT"] = MB2["RUT"].astype(str)+ "-" +MB2["DV"].astype(str)
MB3["RUT"] = MB3["RUT"].astype("float").map('{:.0f}'.format)
MB3["RUT"] = MB3["RUT"].astype(str)+ "-" +MB3["DV"].astype(str)
MB4["RUT"] = MB4["RUT"].astype("float").map('{:.0f}'.format)
MB4["RUT"] = MB4["RUT"].astype(str)+ "-" +MB4["DV"].astype(str)



# %% COLUMNAS UTILES 
MB1 = MB1[['RUT CLIENTE', 'MARCA', 'MODELO', 'PATENTE']]
MB2 = MB2[['RUT','COMUNA', 'MARCA', 'MODELO', 'PATENTE']]
MB3 = MB3[['RUT','COMUNA', 'MARCA', 'MODELO', 'PATENTE']]
MB4 = MB4[['RUT','COMUNA', 'MARCA', 'MODELO', 'PATENTE']]
MB5 = MB5[['RUT','MARCA', 'MODELO', 'PATENTE']]


# %%
MB1.rename(columns={"RUT CLIENTE": "RUT"}, inplace=True)


# %% UNIR 217065
MB = pd.concat([MB1, MB2, MB3, MB4, MB5])

# %% ELIMINAR SOBRANTE
MB.drop_duplicates(inplace=True)
MB.dropna(inplace=True, how='all')

# %%
MB.info()
# %%
MB.to_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\Mercedes y BMW.csv')


# %%
