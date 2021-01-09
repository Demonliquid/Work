# %%
import os
import pandas as pd
import numpy as np


# %% CARGA DE DATOS

# MODELO
base = pd.read_csv(r'D:\Basededatos\esquema.csv')

# PAIS
# HAY FILAS CON COLUMNAS MEZCLADAS
elsalvador =  pd.read_csv(r'D:\Basededatos\Origen\El Salvador.txt', encoding='latin-1')


# %%
elsalvador.to_csv(r'D:\Basededatos\Limpioparaentregar\elsalvador.csv', index=False)

# %%
elsalvador.info()

# %% EQUIVALENCIAS
elsalvador["MERCADO"] = "EL SALVADOR"
elsalvador["CANTIDAD"] = 1
elsalvador.rename(columns={
                'Veh Clase': 'SEGMENTO.1',
                'Veh Marca': 'MARCA',
                'Veh Modelo': 'MODELO',
                'Veh Ano De Fabricacion': 'AÑO',
                'Veh Chasis': 'NUMERO CHASIS / VIN',
                'Veh Motor': 'NUMERO MOTOR',
                'Pro Departamento': 'PROVINCIA',
                'Pro Municipio': 'MUNICIPIO'
                },
                inplace=True)


# %% FORMATO PARA UNIR
columnasutiles = [
                  "MERCADO",
                  "SEGMENTO.1",
                  "MARCA",
                  "MODELO",
                  "AÑO",
                  "CANTIDAD",
                  "NUMERO CHASIS / VIN",
                  "NUMERO MOTOR",
                  "PROVINCIA",
                  "MUNICIPIO"
                  ]
elsalvador = elsalvador[columnasutiles]


# %%
elsalvador["AÑO"] = elsalvador["AÑO"].astype("float").map('{:.0f}'.format)


# %%
elsalvador.info()


# %%
elsalvador.to_csv(r'D:\Basededatos\Limpioparaunir\elsalvador.csv', index=False)

# %%
