# %%
import os
import pandas as pd
import numpy as np
import datetime
import xlrd
from vininfo import Vin


# %% CARGA DE DATOS

# MODELO
base = pd.read_csv(r'D:\Basededatos\esquema.csv')

# PAIS - ORIGINALES
costa_rica = pd.read_csv(r"D:\Basededatos\Limpioparaentregar\costa_rica_bruto.csv")




# %% CAMBIAR POSICION DE CILINDROS
# PROBLEMA: CILINDROS TIENE QUE SER NUMEROS Y POSICION TIENE QUE SER LETRA
cambiarcilindroyposicion = costa_rica.loc[costa_rica["CILINDROS"].astype("str").str.isupper() == True]


# %%
costa_rica = costa_rica.drop(costa_rica[costa_rica["CILINDROS"].str.isalpha() == True].index)


# %%
cambiarcilindroyposicion.rename(columns={
                'CILINDROS': 'cilindros',
                'Posición Cilindros': 'CILINDROS',
                'cilindros': 'CILINDROS',
                },
                inplace=True)


# %% 
costa_rica = pd.concat([costa_rica, cambiarcilindroyposicion], join='outer')
costa_rica.drop(columns=['cilindros'], inplace=True)


# %%
costa_rica.to_csv(r'D:\Basededatos\Limpioparaentregar\costa_rica.csv', index=False)


# %%
costa_rica = pd.read_csv(r'D:\Basededatos\Limpioparaentregar\costa_rica.csv')


# %% EQUIVALENCIAS
costa_rica["MERCADO"] = "COSTA RICA"
costa_rica["CANTIDAD"] = 1
costa_rica["TRANSMISION"].replace('M', 'MANUAL', inplace=True) 
costa_rica["TRANSMISION"].replace('A', 'AUTOMATICO', inplace=True) 
costa_rica["DISPOSICION CILINDROS"] =  costa_rica["Posición Cilindros"].astype("str") + costa_rica["CILINDROS"].astype("str")



costa_rica.rename(columns={
                'MODELO': 'MODELOAREVISAR',
                'CODIGO MARCA': 'MARCA',
                'ESTILO': 'MODELO',
                'Número Motor': 'NUMERO MOTOR',
                'AÑO MODELO': 'AÑO',
                'CILINDRAJE': 'CILINDRADA',
                'TRACCION': 'TRACCION'
                },
                inplace=True)


# %%
costa_rica["CILINDRADA"].replace('nan', None, inplace=True)
costa_rica["CILINDRADA"].replace('NaN', None, inplace=True)

# %%
costa_rica["CILINDRADA"] = costa_rica["CILINDRADA"].astype("float").map('{:.0f}'.format)

# %%
costa_rica["AÑO"] = costa_rica["AÑO"].astype(int)
costa_rica["AÑO"] = costa_rica["AÑO"].astype(str)


# %% AGREGAR MARCAS
marcas = pd.read_excel(r'D:\Basededatos\Origen\Costa Rica\Codigo Marca Costa Rica.xlsx', engine='openpyxl' )


# %%
costa_rica = pd.merge(
    costa_rica,
    marcas[['MARCA', 'Nombre de marca']],
    on='MARCA'
    )


# %%
costa_rica.rename(columns={
                'MARCA': 'CODIGO DE MARCA',
                'Nombre de marca': 'MARCA',
                },
                inplace=True)



# %% GENERAR ORIGEN SEGUN VIN
costa_ricaconvin = costa_rica[costa_rica["IDENTIFICACION DEL VEHICULO"].str.len() == 17]
costa_ricaconvin = costa_ricaconvin[costa_ricaconvin["IDENTIFICACION DEL VEHICULO"].str.contains('Q|O|I', regex=True) == False]
costa_ricaconvin = costa_ricaconvin[costa_ricaconvin["IDENTIFICACION DEL VEHICULO"].str.contains('I|O|Q', regex=True) == False]
costa_ricaconvin = costa_ricaconvin[costa_ricaconvin["IDENTIFICACION DEL VEHICULO"].str.contains('i|o|q', regex=True) == False]
costa_ricaconvin["ORIGEN"] = costa_ricaconvin["IDENTIFICACION DEL VEHICULO"].map(lambda x: Vin(x).country)
costa_ricaconvin['ORIGEN'].replace('China (Mainland)', 'China', inplace=True)
costa_ricaconvin['ORIGEN'].replace('Taiwan, China', 'China', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Cote d'Ivoire", 'Costa de Marfil', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Germany/West Germany", 'Alemania', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Korea (South)", 'Corea del Sur', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Saudi Arabia", 'Arabia Saudita', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"United Kingdom", 'Reino Unido', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Italy", 'Italia', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Greece", 'Grecia', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Belgium", 'Belgica', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"Luxembourg", 'Luxemburgo', inplace=True)
costa_ricaconvin['ORIGEN'].replace(r"United States", 'Estados Unidos', inplace=True)
costa_ricasinvin = pd.concat([costa_rica, costa_ricaconvin]).drop_duplicates(keep=False)
costa_rica = pd.concat([costa_ricaconvin, costa_ricasinvin])


# %%
columnasutiles = [
                  "IDENTIFICACION DEL VEHICULO",
                  "MERCADO",
                  "MARCA",
                  "MODELO",
                  "DISPOSICION CILINDROS",
                  "CILINDRADA",
                  "CILINDROS",
                  "TRACCION",
                  "TRANSMISION",
                  "AÑO",
                  "CANTIDAD",
                  "NUMERO MOTOR",
                  "ORIGEN"]


costa_rica = costa_rica[columnasutiles]


# %%
costa_rica.rename(columns={"MODELO": "MODELO/VERSION", "IDENTIFICACION DEL VEHICULO": "NUMERO CHASIS / VIN"}, inplace=True)
new = costa_rica["MODELO/VERSION"].str.split(" ", n = 1, expand = True)
costa_rica["MODELO"] = new[0]


# %%
costa_rica.info()

# %%
costa_rica.head()

# %%
costa_rica.to_csv(r'D:\Basededatos\Limpioparaunir\costa_rica.csv', index=False)


# %%
