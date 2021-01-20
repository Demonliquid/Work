# %% IMPORTAR LIBRERIAS
import os
import pandas as pd
import numpy as np
import datetime
from vininfo import Vin # ORIGEN Y MARCA
from pyvin import VIN


# %% CARGA DE DATOS
BBDD = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\BBDD.csv')
Definitiva = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\Definitiva.csv')
Mercedesybmw = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\Mercedes y BMW.csv')
seguros = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\seguros.csv')
datosVM = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\datosVM.csv')


# %% RENOMBRAR COLUMNAS
BBDD = BBDD.rename(columns={"MODELO": "MODELO/VERSION"})
Definitiva = Definitiva.rename(columns={"MODELO": "MODELO/VERSION"})
Mercedesybmw = Mercedesybmw.rename(columns={"MODELO": "MODELO/VERSION"})
seguros = seguros.rename(columns={"Modelo": "MODELO/VERSION",
                        "patente": "PATENTE",
                        "comuna": "COMUNA"})
datosVM = datosVM.rename(columns={"MODELO": "MODELO/VERSION"})


# %% COLUMNAS UTILES
BBDD = BBDD[['RUT','MARCA', 'MODELO/VERSION', 'C.C', 'COMBUSTIBLE', 'PATENTE', 'CHASIS', 'COMUNA']]
Definitiva = Definitiva[['RUT','MARCA', 'MODELO/VERSION', 'C.C', 'COMBUSTIBLE', 'PATENTE', 'CHASIS', 'COMUNA']]
Mercedesybmw = Mercedesybmw[['RUT','MARCA', 'MODELO/VERSION' ,'PATENTE', 'COMUNA']]
seguros = seguros[['RUT','MARCA', 'MODELO/VERSION', 'PATENTE', 'COMUNA']]
datosVM = datosVM[['PATENTE', 'SEGMENTO.1', 'MODELO/VERSION', 'VERSION (SALES DESCRIPTION)', 'RUT', 'NUMERO MOTOR', 'AÑO']]


# %% BASE UNIFICADA
base = pd.concat([BBDD, Definitiva, Mercedesybmw, seguros, datosVM])


# %% LIMPIEZA GENERAL BASE UNIFICADA
base.drop_duplicates(inplace=True)
base.dropna(inplace=True, how='all')


# %% CAMBIO NOMBRE COLUMNAS DE BASE UNIFICADA
idx = {'CHASIS': 'NUMERO CHASIS / VIN', 'COMUNA': 'LOCALIDAD'}
base.rename(columns=idx, inplace=True)


# %% PAIS DE ORIGEN DE DATOS
base['MERCADO'] = 'CHILE'


# %% ELIMINAR DATOS SIN PATENTE O CHASIS COMO ELEMENTO INDIVIDUALIZADOR
sinpatente = base["PATENTE"].isna()
sinvin = base["NUMERO CHASIS / VIN"].isna()
base = base.drop(base[sinpatente & sinvin].index)


# %% CONDICIONES DE UN VIN VALIDO
sincaracter = base["NUMERO CHASIS / VIN"].str.isalnum() == True
cantidad = base["NUMERO CHASIS / VIN"].str.len() == 17
letras = base["NUMERO CHASIS / VIN"].str.contains('Q|O|I', regex=True) == False


# %% OBTENER ORIGIN SEGUN VIN
# DIVIDIR BASE EN 2: CON Y SIN VIN
baseconvin = base[sincaracter & cantidad & letras]
basesinvin = pd.concat([base, baseconvin]).drop_duplicates(keep=False)
basesinvin["ORIGEN"] = None
basesinvin["NUMERO CHASIS / VIN"] = None

# OBTENER ORIGEN
baseconvin["ORIGEN"] = baseconvin["NUMERO CHASIS / VIN"].map(lambda x: Vin(x).country)
baseconvin["FABRICANTEVIN"] = baseconvin["NUMERO CHASIS / VIN"].map(lambda x: Vin(x).manufacturer)
#baseconvin["MODELOVIN"] = baseconvin["NUMERO CHASIS / VIN"].map(lambda x: VIN(x).Model)
#baseconvin["AÑOVIN"] = baseconvin["NUMERO CHASIS / VIN"].map(lambda x: VIN(x).ModelYear)
#baseconvin["MODELOVIN"] = baseconvin["NUMERO CHASIS / VIN"].apply(lambda x: VIN(x).Model)
#baseconvin["AÑOVIN"] = baseconvin["NUMERO CHASIS / VIN"].apply(lambda x: VIN(x).ModelYear)

# TRADUCCION MANUAL
baseconvin['ORIGEN'].replace('China (Mainland)', 'China', inplace=True)
baseconvin['ORIGEN'].replace('Taiwan, China', 'China', inplace=True)
baseconvin['ORIGEN'].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
baseconvin['ORIGEN'].replace(r"Germany/West Germany", 'Alemania', inplace=True)
baseconvin['ORIGEN'].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
baseconvin['ORIGEN'].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
baseconvin['ORIGEN'].replace(r"United Kingdom", 'Reino Unido', inplace=True)
baseconvin['ORIGEN'].replace(r"Italy", 'Italia', inplace=True)
baseconvin['ORIGEN'].replace(r"Greece", 'Grecia', inplace=True)
baseconvin['ORIGEN'].replace(r"Belgium", 'Belgica', inplace=True)
baseconvin['ORIGEN'].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
baseconvin['ORIGEN'].replace(r"United States", 'Estados Unidos', inplace=True)
baseconvin['ORIGEN'].replace(r"Japan", 'Japon', inplace=True)
baseconvin['ORIGEN'].replace(r"Czech Republic", 'Republica Checa', inplace=True)
baseconvin['ORIGEN'].replace(r"United Arab Emirates", 'Emiratos Arabes Unidos', inplace=True)
baseconvin['ORIGEN'].replace(r"Ethiopia", 'Etiopia', inplace=True)
baseconvin['ORIGEN'].replace(r"Hungary", 'Hungria', inplace=True)
baseconvin['ORIGEN'].replace(r"Brazil", 'Brasil', inplace=True)
baseconvin['ORIGEN'].replace(r"Spain", 'España', inplace=True)
baseconvin['ORIGEN'].replace(r"France", 'Francia', inplace=True)
baseconvin['ORIGEN'].replace(r"Switzerland", 'Suiza', inplace=True)
baseconvin['ORIGEN'].replace(r"Thailand", 'Tailandia', inplace=True)
baseconvin['ORIGEN'].replace(r"Denmark", 'Dinamarca', inplace=True)
baseconvin['ORIGEN'].replace(r"Finland", 'Finlandia', inplace=True)
baseconvin['ORIGEN'].replace(r"Poland", 'Polonia', inplace=True)
baseconvin['ORIGEN'].replace(r"Myanmar", 'Birmania', inplace=True)
baseconvin['ORIGEN'].replace(r"Ireland", 'Irlanda', inplace=True)
baseconvin['ORIGEN'].replace(r"Netherlands", 'Paises Bajos', inplace=True)
baseconvin['ORIGEN'].replace(r"South Africa", 'Sudafrica', inplace=True)

# BASE CON ORIGEN
base = pd.concat([baseconvin, basesinvin])

# %% ARREGLAR PATENTES CON VALOR "-"" o "??%%??"
# El siguiente codigo elimina donde no hay VIN y mala patente
# Donde hay VIN y mala patente, cambia patente a None
malapatente = (base["PATENTE"] == "-") | (base["PATENTE"] == r"??%%??")
faltachasis = base["NUMERO CHASIS / VIN"].isna()
index = base[malapatente & faltachasis].index
base.drop(index, inplace=True)
base["PATENTE"].replace({"-": None,
                         r"??%%??": None},
                         inplace=True)


# %% LIMPIAR MODELO/VERSION
# EXTRAER CILINDRADA
base["CILINDRADA"] = base["MODELO/VERSION"].str.extract(r'(\d\.\d)', expand=False).str.strip()

# EXTRAER MODELO
new = base["MODELO/VERSION"].str.split(" ", n = 1, expand = True)
base["MODELO"] = new[0]

# %% RESTANDO PATENTES DUPLICADAS
base.drop_duplicates(subset =["PATENTE", "RUT"], 
                     inplace = True) 


# %%
base.to_csv(r'D:\Basededatos\Limpioparaunir\chile BBDD.csv', index=False)

# %%
baseconvin["MODELOVIN"] = baseconvin["NUMERO CHASIS / VIN"].apply(lambda x: VIN(x).Model)

# %%

baseconvin["NUMERO CHASIS / VIN"].head()
# %%
