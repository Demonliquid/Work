# %%
import os
import pandas as pd
import numpy as np


# %% CARGA DE DATOS

# MODELO
base = pd.read_csv(r'D:\Basededatos\esquema.csv')

# PAIS
# HAY FILAS CON COLUMNAS MEZCLADAS
paraguay =  pd.read_csv(r'D:\Basededatos\Origen\Paraguay\Bases Unificadas_Paraguay_Limpio.csv')


# %% ELIMINAR FILAS POR IMPOSIBILIDAD DE ASEGURAR UBICACION
# SE PIERDEN 775 FILAS

# CAMBIAR A FORMATO INPLACE = TRUE
paraguay = paraguay.drop(paraguay[paraguay["Año de fabricacion"].astype("str").str.isalpha() == True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Año de fabricacion"] == "AZUL Y GRIS")==True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Año de fabricacion"] == "GRIS HUMO")==True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Año de fabricacion"] == "VERDE DORADO")==True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Año de fabricacion"] == "VERDE MUSGO")==True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Año de fabricacion"] == "VERDE MUSGO MET")==True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Año de fabricacion"] == "VERDE METALIZADO")==True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Año de fabricacion"] == "VERDE METAL")==True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Año de fabricacion"] == "GRIS PLATA")==True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Año de fabricacion"] == "VINO CLARO")==True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Año de fabricacion"] == "ROJO PERLA")==True].index)
paraguay["Año de fabricacion"].replace('1905-06-27 00:00:00', '1905', inplace=True) 
paraguay["Año de fabricacion"].replace('1905-06-26 00:00:00', '1905', inplace=True) 
paraguay["Año de fabricacion"].replace('1905-06-26 00:00:00', '1905', inplace=True) 
paraguay["Año de fabricacion"].replace('1905-06-28 00:00:00', '1905', inplace=True)
paraguay["Año de fabricacion"].replace('20007', '2007', inplace=True)

# REVER ESTE CODIGO
value_counts = paraguay["Año de fabricacion"].value_counts()
to_remove = value_counts[value_counts == 1].index
paraguay = paraguay[~paraguay["Año de fabricacion"].isin(to_remove)]
# REVER ESTE CODIGO


# %% DATOS LIMPIOS
paraguay.to_csv(r'D:\Basededatos\Limpioparaentregar\paraguay.csv', index=False)


# %%
paraguay = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\paraguay.csv')


# %%
paraguay["Año de fabricacion"] = paraguay["Año de fabricacion"].astype(int)
paraguay["Año de fabricacion"] = paraguay["Año de fabricacion"].astype(str)


# %% EQUIVALENCIAS
paraguay["MERCADO"] = "PARAGUAY"
paraguay["CANTIDAD"] = 1
paraguay.rename(columns={
                'Clase de Automotor': 'SEGMENTO.1',
                'Marca': 'MARCA',
                'Modelo': 'MODELO',
                'País de Fabricación': 'ORIGEN',
                'Año de fabricacion': 'AÑO'},
                inplace=True)


# %% FORMATO PARA UNIR
columnasutiles = [
                  "MERCADO",
                  "SEGMENTO.1",
                  "MARCA",
                  "MODELO",
                  "AÑO",
                  "CANTIDAD",
                  "ORIGEN"
                  ]
paraguay = paraguay[columnasutiles]


# %%

# %%
paraguay.to_csv(r'D:\Basededatos\Limpioparaunir\paraguay.csv', index=False)


# %%
paraguay =  pd.read_csv(r'D:\Basededatos\Limpioparaunir\paraguay.csv')

# %%
paraguay.info()

# %%
paraguay.head()
# %%
