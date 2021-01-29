# %%
import os
import pandas as pd
import numpy as np
import re


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
paraguay = paraguay.drop(paraguay[(paraguay["Clase de Automotor"] == "DORADO")==True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Clase de Automotor"] == "NEGRO/ROJO")==True].index)
paraguay = paraguay.drop(paraguay[(paraguay["Clase de Automotor"] == "2016-09-20 00:00:00")==True].index)
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
paraguay["Año de fabricacion"] = paraguay["Año de fabricacion"].astype(int)
paraguay["Año de fabricacion"] = paraguay["Año de fabricacion"].astype(str)


# %% EQUIVALENCIAS
paraguay["MERCADO"] = "PARAGUAY"
paraguay["CANTIDAD"] = 1
paraguay.rename(columns={
                'Clase de Automotor': 'SEGMENTO.1',
                'Marca': 'MARCA',
                'Modelo': 'MODELO/VERSION',
                'País de Fabricación': 'ORIGEN',
                'Año de fabricacion': 'AÑO'},
                inplace=True)


# %% FORMATO PARA UNIR
columnasutiles = [
                  "MERCADO",
                  "SEGMENTO.1",
                  "MARCA",
                  "MODELO/VERSION",
                  "AÑO",
                  "CANTIDAD",
                  "ORIGEN"
                  ]
paraguay = paraguay[columnasutiles]


# %%
paraguay["CILINDRADA"] = paraguay["MODELO/VERSION"].str.extract(r'(\d\.\d)', expand=False).str.strip()
paraguay["CILINDRADA"].replace(r'', None)


# %% LIMPIAR MODELO

# GENERAL
new = paraguay["MODELO/VERSION"].str.split(" ", n = 1, expand = True)
paraguay["MODELO"] = new[0] 
paraguay["MODELO"].replace({"SIN": None}, inplace=True)


# NEW HOLLAND
listamodelo = r'''(TL 250|TL 200|TL 150|TL 125|TL 110|TL 100|TL 95|TL 95 EXITUS|TL 90|TL 85|TL 85 EXITUS|TL 80|TL 75|TL 75 EXITUS|TL 70|TL 65|TL - 12)'''
paraguay["MODELO2"] = paraguay["MODELO/VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = paraguay["MODELO2"].notna()
paraguay.loc[condicion, "MODELO"] = paraguay.loc[condicion, "MODELO2"]
paraguay = paraguay[["MERCADO", "SEGMENTO.1", "MARCA", "MODELO", "MODELO/VERSION", "AÑO", "ORIGEN","CILINDRADA", "CANTIDAD"]]
paraguay["MODELO"].replace({"TL - 12":"Renault 12"}, inplace=True)


# STAR
listamodelo = r'''(SK DESER|SK SUPER|SK CARGA|SK SUPERTUIS|SK BR200|SK 1722|SK 250|SK 200|SK 150|SK 125|SK 110|SK 100)'''
paraguay["MODELO2"] = paraguay["MODELO/VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = paraguay["MODELO2"].notna()
paraguay.loc[condicion, "MODELO"] = paraguay.loc[condicion, "MODELO2"]
paraguay = paraguay[["MERCADO", "SEGMENTO.1", "MARCA", "MODELO", "MODELO/VERSION", "AÑO", "ORIGEN","CILINDRADA", "CANTIDAD"]]


# TOYOTA
listamodelo = r'''(ALLION|FUNCARGO)'''
paraguay["MODELO2"] = paraguay["MODELO/VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = paraguay["MODELO2"].notna()
paraguay.loc[condicion, "MODELO"] = paraguay.loc[condicion, "MODELO2"]
paraguay = paraguay[["MERCADO", "SEGMENTO.1", "MARCA", "MODELO", "MODELO/VERSION", "AÑO", "ORIGEN","CILINDRADA", "CANTIDAD"]]

paraguay["MODELO"].replace({"VITZ": "YARIS",
                            "IST": "Urban Cruiser",
                            "IST F L": "Urban Cruiser",
                            "IST SCION": "Urban Cruiser"}, inplace=True)


# HONDA
listamodelo = r'''(GL 1800|GL 1500|GL 1200|GL 1000|GL 550|GL 500|GL 450|GL 420|GL 400|GL 350|GL 320|GL 305|GL 244|GL 200|GL 150|GL 125|GL 110|GL 100| GL 90)'''
paraguay["MODELO2"] = paraguay["MODELO/VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = paraguay["MODELO2"].notna()
paraguay.loc[condicion, "MODELO"] = paraguay.loc[condicion, "MODELO2"]
paraguay = paraguay[["MERCADO", "SEGMENTO.1", "MARCA", "MODELO", "MODELO/VERSION", "AÑO", "ORIGEN","CILINDRADA", "CANTIDAD"]]


# MONDIAL
listamodelo = r'''(MD 920|MD 200|MD 150|MD 125|MD 100)'''
paraguay["MODELO2"] = paraguay["MODELO/VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = paraguay["MODELO2"].notna()
paraguay.loc[condicion, "MODELO"] = paraguay.loc[condicion, "MODELO2"]
paraguay = paraguay[["MERCADO", "SEGMENTO.1", "MARCA", "MODELO", "MODELO/VERSION", "AÑO", "ORIGEN","CILINDRADA", "CANTIDAD"]]


# KENTON
listamodelo = r'''(GTR Z|GTR 200|GTR 150)'''
paraguay["MODELO2"] = paraguay["MODELO/VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = paraguay["MODELO2"].notna()
paraguay.loc[condicion, "MODELO"] = paraguay.loc[condicion, "MODELO2"]
paraguay = paraguay[["MERCADO", "SEGMENTO.1", "MARCA", "MODELO", "MODELO/VERSION", "AÑO", "ORIGEN","CILINDRADA", "CANTIDAD"]]


# FIAT
listamodelo = r'''(PREMIO)'''
paraguay["MODELO2"] = paraguay["MODELO/VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = paraguay["MODELO2"].notna()
paraguay.loc[condicion, "MODELO"] = paraguay.loc[condicion, "MODELO2"]
paraguay = paraguay[["MERCADO", "SEGMENTO.1", "MARCA", "MODELO", "MODELO/VERSION", "AÑO", "ORIGEN","CILINDRADA", "CANTIDAD"]]

paraguay["MODELO"].replace({"PREMIO": "DUNA"}, inplace=True)


# VOLKSWAGEN
listamodelo = r'''(GOL)'''
paraguay["MODELO2"] = paraguay["MODELO/VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = paraguay["MODELO2"].notna()
paraguay.loc[condicion, "MODELO"] = paraguay.loc[condicion, "MODELO2"]
paraguay = paraguay[["MERCADO", "SEGMENTO.1", "MARCA", "MODELO", "MODELO/VERSION", "AÑO", "ORIGEN","CILINDRADA", "CANTIDAD"]]


# VOLKSWAGEN
listamodelo = r'''(SUNNY)'''
paraguay["MODELO2"] = paraguay["MODELO/VERSION"].str.extract(listamodelo, expand=False).str.strip()
condicion = paraguay["MODELO2"].notna()
paraguay.loc[condicion, "MODELO"] = paraguay.loc[condicion, "MODELO2"]
paraguay = paraguay[["MERCADO", "SEGMENTO.1", "MARCA", "MODELO", "MODELO/VERSION", "AÑO", "ORIGEN","CILINDRADA", "CANTIDAD"]]

paraguay["MODELO"].replace({"SUNNY": "SENTRA"}, inplace=True)



# %%
condicion = paraguay["MODELO"] == "PLATZ"
dict(paraguay["MODELO/VERSION"][condicion].value_counts())

# %%
paraguay[condicion].head()

# %%
dict(paraguay["MODELO"].value_counts())


# %%
paraguay.rename(coumns={"CILINDRADA": "MOTOR LITROS"}, inplace=True)


# %%
paraguay.to_csv(r'D:\Basededatos\Limpioparaunir\paraguay.csv', index=False)
