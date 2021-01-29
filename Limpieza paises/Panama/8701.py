# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DE DATOS
path = r'D:\Basededatos\Origen\Panama\8701'
os.chdir(path)
files = os.listdir(path)
files

files_xls = [f for f in files if f[-3:] == 'xls']
files_xls


panama = pd.DataFrame()


for f in files_xls:
    data = pd.read_excel(f)
    panama = pd.concat([panama , data], ignore_index=True, join='outer')


# %% COLUMNAS UTILES
panama["DESCRIPCION"] = panama["Unnamed: 21"][4:]
panama["FECHA"] = panama["Unnamed: 3"][4:]
panama = panama[["DESCRIPCION","FECHA"]]


# %%
panama.dropna(inplace=True, how="all")


# %% GUARDAR AVANCE
panama.to_csv(r'D:\Basededatos\Origen\Panama\8701\Bruto\todojunto.csv', index=False, header=True, sep=",")


# %% CAMPOS PARA UNIR
# CILINDRADA
panama["CILINDRADA"] = panama["DESCRIPCION"].str.extract(r'(\d\.\d)', expand=False).str.strip()# %%


# %% SEGMENTO.1
listasegmento = r'''(CABEZAL|BULLDOZER|TARACTOR|TRACTRO|VAGONETA|VOLQUETE|TARCTOR|TRACTROC|Mula|TRACTO|TRATOR|motocultores|GRUA|CARGADOR|ZANJADORA|Cabezal|MINICARGADORA|TRAILER|tracto mulita|AUTOMOVIL|TRACTO CAMIÓN|tractor|cabezal|Camión|Tractor|MINI BIKES|MTOS|MOTACICLETA|TRANSPORTE LIGERO|MPTOCICLETA|MTOCICLETA|MOTCICLETA|FORWEEL|FOUR WHELL|4 WHEEL|FOUR-WHEELS|.4WHEEL.|TODO TERRENO|VAN|MINI VANS|BUS|MICROBUS|AUTOBUS|BUSITO|MOTICICLETA|CARRITO DE GOLF|SCCOTER|BOCICLETA|BICILETA|FOUR WHEEL|FOURWHEEL|4WHEELS|EQUIPO PESADO|TRACTROR|TRUCK|UTILITARIO|FURGON|MONOCULTOR|TRACOR|TACTOR|PICK-UP|PATINETA|CAMION|ASTILADORA|REMOLQUE|MOTOCICLETA|MOTO|TRACTOR|KAISE|KAISER|TRACOTR|MULA|BICICLETA|TRAVEL TRAILER|OTAWA|OTTAWA|CAMION VOLQUETE|PATINES|FOUR WEEL|TRACOTR|SCOOTER)'''
panama["SEGMENTO.1"] = panama["DESCRIPCION"].str.extract(listasegmento, expand=False).str.strip()


# %% VERIFICACION SEGMENTO
#condicion = panama["SEGMENTO.1"].isna()
#panama[condicion][50:100]






# %% MARCA
# BUSCAR MARCA EN TEXTO
regex = r'MARCA\s+\b(\w+)\b'
regex2 = r'MARCA:\s+\b(\w+)\b'
regex3 = r'marca\s+\b(\w+)\b'
regex4 = r'marca:\s+\b(\w+)\b'
regex5 = r'Marca\s+\b(\w+)\b'
regex6 = r'Marca:\s+\b(\w+)\b'
listamarca = r'''(vikino|KIA|HYUNDAI|FREIGHTLINER|INTERNATIONAL|CAPACITY|HERO|yamaha|suzuki|kawasaki|SUZUKI|Suzuki|BISEK|YAMAHA|JOHN DEERE|PRATO FORNE|KAWWASAKI|HENGNIU|FREIGHT LINER|FORD|HONDA|KAWASAKI|vikyno|AVA)'''


panama["MARCA"] = panama["DESCRIPCION"].str.extract(regex, expand=False).str.strip()
panama["MARCA2"] = panama["DESCRIPCION"].str.extract(regex2, expand=False).str.strip()
panama["MARCA3"] = panama["DESCRIPCION"].str.extract(regex3, expand=False).str.strip()
panama["MARCA4"] = panama["DESCRIPCION"].str.extract(regex4, expand=False).str.strip()
panama["MARCA5"] = panama["DESCRIPCION"].str.extract(regex5, expand=False).str.strip()
panama["MARCA6"] = panama["DESCRIPCION"].str.extract(regex6, expand=False).str.strip()
panama["MARCA7"] = panama["DESCRIPCION"].str.extract(listamarca, expand=False).str.strip()

# UNIR EN UNICA COLUMNA
condicion = panama["MARCA2"].notna()
condicion2 = panama["MARCA3"].notna()
condicion3 = panama["MARCA4"].notna()
condicion4 = panama["MARCA5"].notna()
condicion5 = panama["MARCA6"].notna()
condicion6 = panama["MARCA7"].notna()


panama.loc[condicion, "MARCA"] = panama.loc[condicion, "MARCA2"]
panama.loc[condicion2, "MARCA"] = panama.loc[condicion2, "MARCA3"]
panama.loc[condicion3, "MARCA"] = panama.loc[condicion3, "MARCA4"]
panama.loc[condicion4, "MARCA"] = panama.loc[condicion4, "MARCA5"]
panama.loc[condicion5, "MARCA"] = panama.loc[condicion5, "MARCA6"]
panama.loc[condicion6, "MARCA"] = panama.loc[condicion6, "MARCA7"]


panama = panama[["FECHA", "DESCRIPCION", "CILINDRADA", "SEGMENTO.1", "MARCA"]]



# %% VERIFICACION MARCA
#tienemarca = r'''(MARCA|marca|MARCA:|marca:|Marca)'''
#panama["verificacionmarca"] = panama["DESCRIPCION"].str.extract(tienemarca, expand=False).str.strip()
#condicion = panama["verificacionmarca"].notna() & panama["MARCA"].isna()
#panama[condicion]


# %% CILINDROS.1
regex = r'(\d+\d)?\S*CC'
regex2 = r'(\d+\d)?\S*C.C'
regex3 = r'(\d+\d)?\S*C.C.'
regex4 = r'(\d+\d)?\S*cc'
regex5 = r'(\d+\d)?\S*c.c'
regex6 = r'(\d+\d)?\S*c.c.'
regex7 = r'(\d+\d)?\S* CC'
regex8 = r'(\d+\d)?\S* C.C'
regex9 = r'(\d+\d)?\S* C.C.'
regex10 = r'(\d+\d)?\S* cc'
regex11 = r'(\d+\d)?\S* c.c'
regex12 = r'(\d+\d)?\S* c.c.'

panama["CILINDROS.1"] = panama["DESCRIPCION"].str.extract(regex, expand=False).str.strip()
panama["CILINDROS.2"] = panama["DESCRIPCION"].str.extract(regex2, expand=False).str.strip()
panama["CILINDROS.3"] = panama["DESCRIPCION"].str.extract(regex3, expand=False).str.strip()
panama["CILINDROS.4"] = panama["DESCRIPCION"].str.extract(regex4, expand=False).str.strip()
panama["CILINDROS.5"] = panama["DESCRIPCION"].str.extract(regex5, expand=False).str.strip()
panama["CILINDROS.6"] = panama["DESCRIPCION"].str.extract(regex6, expand=False).str.strip()
panama["CILINDROS.7"] = panama["DESCRIPCION"].str.extract(regex7, expand=False).str.strip()
panama["CILINDROS.8"] = panama["DESCRIPCION"].str.extract(regex8, expand=False).str.strip()
panama["CILINDROS.9"] = panama["DESCRIPCION"].str.extract(regex9, expand=False).str.strip()
panama["CILINDROS.10"] = panama["DESCRIPCION"].str.extract(regex10, expand=False).str.strip()
panama["CILINDROS.11"] = panama["DESCRIPCION"].str.extract(regex11, expand=False).str.strip()
panama["CILINDROS.12"] = panama["DESCRIPCION"].str.extract(regex12, expand=False).str.strip()


# UNIR EN UNICA COLUMNA
condicion = panama["CILINDROS.2"].notna()
condicion2 = panama["CILINDROS.3"].notna()
condicion3 = panama["CILINDROS.4"].notna()
condicion4 = panama["CILINDROS.5"].notna()
condicion5 = panama["CILINDROS.6"].notna()
condicion6 = panama["CILINDROS.7"].notna()
condicion7 = panama["CILINDROS.8"].notna()
condicion8 = panama["CILINDROS.9"].notna()
condicion9 = panama["CILINDROS.10"].notna()
condicion10 = panama["CILINDROS.11"].notna()
condicion11 = panama["CILINDROS.12"].notna()

panama.loc[condicion, "CILINDROS.1"] = panama.loc[condicion, "CILINDROS.2"]
panama.loc[condicion2, "CILINDROS.1"] = panama.loc[condicion2, "CILINDROS.3"]
panama.loc[condicion3, "CILINDROS.1"] = panama.loc[condicion3, "CILINDROS.4"]
panama.loc[condicion4, "CILINDROS.1"] = panama.loc[condicion4, "CILINDROS.5"]
panama.loc[condicion5, "CILINDROS.1"] = panama.loc[condicion5, "CILINDROS.6"]
panama.loc[condicion6, "CILINDROS.1"] = panama.loc[condicion6, "CILINDROS.7"]
panama.loc[condicion7, "CILINDROS.1"] = panama.loc[condicion7, "CILINDROS.8"]
panama.loc[condicion8, "CILINDROS.1"] = panama.loc[condicion8, "CILINDROS.9"]
panama.loc[condicion9, "CILINDROS.1"] = panama.loc[condicion9, "CILINDROS.10"]
panama.loc[condicion10, "CILINDROS.1"] = panama.loc[condicion10, "CILINDROS.11"]
panama.loc[condicion11, "CILINDROS.1"] = panama.loc[condicion11, "CILINDROS.12"]


panama = panama[["FECHA", "DESCRIPCION", "CILINDRADA", "SEGMENTO.1", "MARCA", "CILINDROS.1"]]


# %% VERIFICACION CILINDROS.1
#condicion = panama["CILINDROS.1"].isna()
#panama[condicion][50:100]


# %% MODELO
# BUSCAR MODELO EN TEXTO
# BUSCAR TEXTO DESPUSE DE LA PALABRA MODELO
regex = r'MODELO\s+\b(\w+)\b'
regex2 = r'MODELO:\s+\b(\w+)\b'
regex3 = r'MODELO,\s+\b(\w+)\b'
regex4 = r'modelo\s+\b(\w+)\b'
regex5 = r'modelo:\s+\b(\w+)\b'
regex6 = r'modelo,\s+\b(\w+)\b'
regex7 = r'Modelo\s+\b(\w+)\b'
regex8 = r'Modelo:\s+\b(\w+)\b'
regex9 = r'Modelo,\s+\b(\w+)\b'
regex10 = r'MODEL\s+\b(\w+)\b'
listamodelo = r'''(HIACE|HI ACE|W41|COASTER|L300|H-1)'''

# APLICAR CADA REGEX
panama["MODELO"] = panama["DESCRIPCION"].str.extract(regex, expand=False).str.strip()
panama["MODELO2"] = panama["DESCRIPCION"].str.extract(regex2, expand=False).str.strip()
panama["MODELO3"] = panama["DESCRIPCION"].str.extract(regex3, expand=False).str.strip()
panama["MODELO4"] = panama["DESCRIPCION"].str.extract(regex4, expand=False).str.strip()
panama["MODELO5"] = panama["DESCRIPCION"].str.extract(regex5, expand=False).str.strip()
panama["MODELO6"] = panama["DESCRIPCION"].str.extract(regex6, expand=False).str.strip()
panama["MODELO7"] = panama["DESCRIPCION"].str.extract(regex7, expand=False).str.strip()
panama["MODELO8"] = panama["DESCRIPCION"].str.extract(regex8, expand=False).str.strip()
panama["MODELO9"] = panama["DESCRIPCION"].str.extract(regex9, expand=False).str.strip()
panama["MODELO10"] = panama["DESCRIPCION"].str.extract(regex10, expand=False).str.strip()
panama["MODELO11"] = panama["DESCRIPCION"].str.extract(listamodelo, expand=False).str.strip()

# CASO ESPECIAL TRACTORES
tractores = (panama["SEGMENTO.1"] == "TRACTO") & (panama["MODELO"].isna())
panama[tractores]["MODELO"] = panama["DESCRIPCION"].str.extract(r'SERIE\s+\b(\w+)\b', expand=False).str.strip()
panama[tractores]["MODELO"] = panama["DESCRIPCION"].str.extract(r'SERIE NO.\s+\b(\w+)\b', expand=False).str.strip()
panama[tractores]["MODELO"] = panama["DESCRIPCION"].str.extract(r'SERIE#\s+\b(\w+)\b', expand=False).str.strip()


# UNIR EN UNICA COLUMNA
condicion = panama["MODELO2"].notna()
condicion2 = panama["MODELO3"].notna()
condicion3 = panama["MODELO4"].notna()
condicion4 = panama["MODELO5"].notna()
condicion5 = panama["MODELO6"].notna()
condicion6 = panama["MODELO7"].notna()
condicion7 = panama["MODELO8"].notna()
condicion8 = panama["MODELO9"].notna()
condicion9 = panama["MODELO10"].notna()
condicion10 = panama["MODELO11"].notna()


panama.loc[condicion, "MODELO"] = panama.loc[condicion, "MODELO2"]
panama.loc[condicion2, "MODELO"] = panama.loc[condicion2, "MODELO3"]
panama.loc[condicion3, "MODELO"] = panama.loc[condicion3, "MODELO4"]
panama.loc[condicion4, "MODELO"] = panama.loc[condicion4, "MODELO5"]
panama.loc[condicion5, "MODELO"] = panama.loc[condicion5, "MODELO6"]
panama.loc[condicion6, "MODELO"] = panama.loc[condicion6, "MODELO7"]
panama.loc[condicion7, "MODELO"] = panama.loc[condicion7, "MODELO8"]
panama.loc[condicion8, "MODELO"] = panama.loc[condicion8, "MODELO9"]
panama.loc[condicion9, "MODELO"] = panama.loc[condicion9, "MODELO10"]
panama.loc[condicion10, "MODELO"] = panama.loc[condicion10, "MODELO11"]


panama = panama[["FECHA", "DESCRIPCION", "CILINDRADA", "SEGMENTO.1", "MARCA", "CILINDROS.1", "MODELO"]]


# %% VERIFICACION MODELO
#condicion = panama["MODELO"].isna()
#panama[condicion][500:550]


# %% VIN O SERIES
# BUSCAR TEXTO DESPUSE DE LA PALABRA VIN
regex1 = r'VIN\s+\b(\w+)\b'
regex2 = r'VIN:\s+\b(\w+)\b'
regex3 = r'CHASIS\s+\b(\w+)\b'
regex4 = r'CHARSIS\s+\b(\w+)\b'

# APLICAR CADA REGEX
panama["NUMERO CHASIS / VIN"] = panama["DESCRIPCION"].str.extract(regex1, expand=False).str.strip()
panama["NUMERO CHASIS / VIN2"] = panama["DESCRIPCION"].str.extract(regex2, expand=False).str.strip()
panama["NUMERO CHASIS / VIN3"] = panama["DESCRIPCION"].str.extract(regex3, expand=False).str.strip()
panama["NUMERO CHASIS / VIN4"] = panama["DESCRIPCION"].str.extract(regex4, expand=False).str.strip()


# UNIR EN UNICA COLUMNA
condicion = panama["NUMERO CHASIS / VIN2"].notna()
condicion2 = panama["NUMERO CHASIS / VIN3"].notna()
condicion3 = panama["NUMERO CHASIS / VIN4"].notna()

panama.loc[condicion, "NUMERO CHASIS / VIN"] = panama.loc[condicion, "NUMERO CHASIS / VIN2"]
panama.loc[condicion2, "NUMERO CHASIS / VIN"] = panama.loc[condicion2, "NUMERO CHASIS / VIN3"]
panama.loc[condicion3, "NUMERO CHASIS / VIN"] = panama.loc[condicion3, "NUMERO CHASIS / VIN4"]

panama = panama[["FECHA", "DESCRIPCION", "CILINDRADA", "SEGMENTO.1", "MARCA", "CILINDROS.1", "MODELO", "NUMERO CHASIS / VIN"]]


# %% transmision
listatransmision = r'''(MANUAL|AUTOMATICO)'''
panama["TRANSMISION"] = panama["DESCRIPCION"].str.extract(listatransmision, expand=False).str.strip()
panama = panama[["FECHA", "DESCRIPCION", "CILINDRADA", "SEGMENTO.1", "MARCA", "CILINDROS.1", "MODELO", "NUMERO CHASIS / VIN", "TRANSMISION"]]


# %% COMBUSTIBLE
listacombustible = r'''(DIESEL|GASOLINA)'''
panama["COMBUSTIBLE"] = panama["DESCRIPCION"].str.extract(listacombustible, expand=False).str.strip()
panama = panama[["FECHA", "DESCRIPCION", "CILINDRADA", "SEGMENTO.1", "MARCA", "CILINDROS.1", "MODELO", "NUMERO CHASIS / VIN", "TRANSMISION", "COMBUSTIBLE"]]


# %% MOTOR
regex1 = r'MOTOR\s+\b(\w+)\b'
panama["NUMERO MOTOR"] = panama["DESCRIPCION"].str.extract(regex1, expand=False).str.strip()
panama = panama[["FECHA", "DESCRIPCION", "CILINDRADA", "SEGMENTO.1", "MARCA", "CILINDROS.1", "MODELO", "NUMERO CHASIS / VIN", "TRANSMISION", "COMBUSTIBLE", "NUMERO MOTOR"]]

# %% CILINDROS
regex1 = r'(\w+)\s+CILINDROS'
regex2 = r'(\w+)\s+CILINDRO'
regex3 = r'(\d+)+CIL'
regex4 = r'(\d+)+CILS'

panama["CILINDROS"] = panama["DESCRIPCION"].str.extract(regex1, expand=False).str.strip()
panama["CILINDROS2"] = panama["DESCRIPCION"].str.extract(regex2, expand=False).str.strip()
panama["CILINDROS3"] = panama["DESCRIPCION"].str.extract(regex3, expand=False).str.strip()
panama["CILINDROS4"] = panama["DESCRIPCION"].str.extract(regex4, expand=False).str.strip()

condicion = panama["CILINDROS2"].notna()
condicion2 = panama["CILINDROS3"].notna()
condicion3 = panama["CILINDROS4"].notna()



panama.loc[condicion, "CILINDROS"] = panama.loc[condicion, "CILINDROS2"]
panama.loc[condicion2, "CILINDROS"] = panama.loc[condicion2, "CILINDROS3"]
panama.loc[condicion3, "CILINDROS"] = panama.loc[condicion3, "CILINDROS4"]



panama = panama[["FECHA", "DESCRIPCION", "CILINDRADA", "SEGMENTO.1", "MARCA", "CILINDROS.1", "MODELO", "NUMERO CHASIS / VIN", "CILINDROS"]]


# %%
pd.set_option('display.max_colwidth', -1)


#%%
condicion = (panama["MARCA"].isna()) & (panama["SEGMENTO.1"].notna())
panama[condicion]


# %%
panama.to_csv(r'D:\Basededatos\Limpioparaentregar\panama\8700.csv', index=False)


# %%
