# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DE DATOS

# MODELO
base = pd.read_csv(r'D:\Basededatos\esquema.csv')

# PAIS 
# SE PIERDEN 3 LINEAS, DEJAR O AGREGAR MANUALMENTE
guatemala = pd.read_csv(r'D:\Basededatos\Origen\Guatemala 2020.txt',
                        names= ["ANIO_ALZA", "MES", "NOMBRE_DEPARTAMENTO", "NOMBRE_MUNICIPIO", "MODELO_VEHICULO", "LINEA_VEHICULO", "TIPO_VEHICULO", "USO_VEHICULO", "MARCA_VEHICULO", "CANTIDAD"],
                        quotechar='"',
                        sep="|",
                        error_bad_lines=False,
                        engine='python')


# %% ARGEGA LINEAS PERDIDAS
datosperdidos = pd.DataFrame(
    {"ANIO_ALZA": [1993, 1995, 1994],
    "MES": [8, 5, 11],
    "NOMBRE_DEPARTAMENTO": ["ZACAPA", "GUATEMALA", "GUATEMALA"],
    "NOMBRE_MUNICIPIO": ["ZACAPA", "SAN MIGUEL PETAPA", "GUATEMALA"],
    "MODELO_VEHICULO": [1989, 1995, 1995],
    "LINEA_VEHICULO": [r'"E" 4WD', r'"H100 DLX', r'"H100 DLX'],
    "TIPO_VEHICULO": ["PICK UP", "PANEL", "PANEL"],
    "USO_VEHICULO": ["PARTICULAR", "PARTICULAR", "PARTICULAR"],
    "MARCA_VEHICULO": ["NISSAN", "HYUNDAI", "HYUNDAI"],
    "CANTIDAD": [1, 1, 1]}
    )
guatemala = guatemala.append(datosperdidos)


# %% 49005 autos con MODELO_VEHICULO = '1980 o menor'
guatemala["MODELO_VEHICULO"].replace('1980 o menor', '1980', inplace=True) 


# %% DATOS LIMPIOS
guatemala.to_csv(r'D:\Basededatos\Limpioparaentregar\guatemala.csv', index=False)


# %% EQUIVALENCIA
guatemala["MERCADO"] = "GUATEMALA"
guatemala.rename(columns={
                'TIPO_VEHICULO': 'SEGMENTO.1',
                'MARCA_VEHICULO': 'MARCA',
                'LINEA_VEHICULO': 'MODELO',
                'MODELO_VEHICULO': 'AÑO',
                'CANTIDAD': 'FLOTA 2019',
                'NOMBRE_DEPARTAMENTO': 'PROVINCIA',
                'NOMBRE_MUNICIPIO': 'LOCALIDAD'},
                inplace=True)


# %% FORMATO PARA UNIR
columnasutiles = [
                  "MERCADO",
                  "SEGMENTO.1",
                  "MARCA",
                  "MODELO",
                  "AÑO",
                  "FLOTA 2019",
                  'PROVINCIA',
                  'LOCALIDAD']

guatemala = guatemala[columnasutiles]


# %%
guatemala.info()


# %%
guatemala.to_csv(r'D:\Basededatos\Limpioparaunir\guatemala.csv', index=False)


# %%
