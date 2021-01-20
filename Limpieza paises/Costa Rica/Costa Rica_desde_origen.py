# %%
import os
import pandas as pd
import numpy as np
import datetime
import xlrd


# %% CARGA DE DATOS
# PROBLEMA: MISMO PAIS EN DISTINTOS ARCHIVOS

# MODELO
base = pd.read_csv(r'D:\Basededatos\esquema.csv')

# PAIS - ORIGINALES
costa_rica0 = pd.read_excel(r"D:\Basededatos\Origen\Costa Rica\Comparto_'Vehiculos_8701_8702_8705_8706_y_87011_segun_ID'_contigo_Costa_Rica.xlsx", sheet_name="SIA", engine='openpyxl')
costa_rica1 = pd.read_excel(r"D:\Basededatos\Origen\Costa Rica\Comparto_'Vehiculos_8701_8702_8705_8706_y_87011_segun_ID'_contigo_Costa_Rica.xlsx", sheet_name="TICA", engine='openpyxl')
costa_rica2 = pd.read_excel(r"D:\Basededatos\Origen\Costa Rica\Vehiculos (8703 y 8704) segun ID_Costa_Rica.xlsx", engine='openpyxl')


# %% ARREGLAR COLUMNAS ORIGINALES
# PROBLEMA: UNO DE LOS ARCHIVOS TIENE COLUMNAS DIFERENTES
costa_rica1.rename(columns={
                'Identificación Vehículo': 'IDENTIFICACION DEL VEHICULO',
                'Marca vehículo': 'CODIGO MARCA',
                'Velocidades': 'VELOCIDADES',
                'transmisión': 'TRANSMISION',
                'Tipo techo': 'TECHO',
                'peso bruto': 'PESO BRUTO',
                'Modelo': 'MODELO',
                'Estilo': 'ESTILO',
                'año modelo': 'AÑO MODELO',
                },
                inplace=True)

# ARREGLAR FORMATO
costa_rica0['VELOCIDADES'].astype('object', copy=False)
costa_rica0['TECHO'].astype('object', copy=False)
costa_rica0['PUERTAS'].astype('object', copy=False)
costa_rica0['PESO BRUTO'].astype('object', copy=False)
costa_rica0['Cantidad Pasajeros'].astype('object', copy=False)
costa_rica0['AÑO MODELO'].astype('object', copy=False)

costa_rica1['VELOCIDADES'].astype('object', copy=False)
costa_rica1['TECHO'].astype('object', copy=False)
costa_rica1['PUERTAS'].astype('object', copy=False)
costa_rica1['PESO BRUTO'].astype('object', copy=False)
costa_rica1['Cantidad Pasajeros'].astype('object', copy=False)
costa_rica1['AÑO MODELO'].astype('object', copy=False)


# %% LIMPIEZA DE DUPLICADOS - TIENEN DATOS INDIVIDUALIZADORES
costa_rica0.drop_duplicates(inplace=True)
costa_rica1.drop_duplicates(inplace=True)
costa_rica2.drop_duplicates(inplace=True)


# %% UNIR ORIGINALES
costa_rica = pd.concat([costa_rica0, costa_rica1, costa_rica2], ignore_index=True, join='outer')


# %% ELIMINAR COLUMANS SOBRANTES
sobrante = ["Tipo moto",
            "Tiempos",
            "Tipo Cabina",
            "N♪mero Clase",
            "Color",
            "Cilindrada",
            "cm cúbicos",
            "carrocería",
            "Codigo Categor",
            "Categoría Vehiculo",
            "tipo combustible",
            "PARTIDA ARANCELARIA",
            "Estado de la Mercancia"
            ]

costa_rica.drop(columns=sobrante,
         inplace=True)


# %%
costa_rica.drop_duplicates(inplace=True)


# %% LIMPIEZA GENERAL
# Tiene valores de puro espacio en Año
# Tiene algunos valores mezclados

filasconespacio = costa_rica[costa_rica["AÑO MODELO"].astype("str").str.isspace() == True]
costa_rica = costa_rica.drop(costa_rica[(costa_rica["AÑO MODELO"].astype("str").str.isspace())==True].index)
costa_rica = costa_rica.drop(costa_rica[(costa_rica["AÑO MODELO"].astype("str").str.isupper())==True].index)
filasconespacio["AÑO MODELO"] = 0
costa_rica = pd.concat([costa_rica, filasconespacio], ignore_index=True, join='outer')


# %%
costa_rica.to_csv(r'D:\Basededatos\Limpioparaentregar\costa_rica_bruto.csv', index=False)

# %%
