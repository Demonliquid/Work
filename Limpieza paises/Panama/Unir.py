# %%
import os
import pandas as pd
import numpy as np
import datetime


# %% CARGA DE DATOS
path = r'D:\Basededatos\Limpioparaentregar\panama'
os.chdir(path)
files = os.listdir(path)
files

files_xls = [f for f in files if f[-3:] == 'csv']
files_xls


panama = pd.DataFrame()


for f in files_xls:
    data = pd.read_csv(f)
    panama = pd.concat([panama , data], ignore_index=True, join='outer')

# %%
panama = panama[["DESCRIPCION", "CILINDRADA", "SEGMENTO.1", "MARCA", "CILINDROS.1", "MODELO", "NUMERO CHASIS / VIN", "CILINDROS"]]

# %%
panama["MERCADO"] = "PANAMA"

# %%
panama["SEGMENTO.1"].replace({"TRACTO": "TRACTOR", "Tractor": "TRACTOR"}, inplace=True)


# %%
panama.to_csv(r'D:\Basededatos\Limpioparaunir\panama.csv', index=False)

# %%
dict(panama["SEGMENTO.1"].value_counts())
# %%
panama.info()

# %%
pd.set_option('display.max_colwidth', -1)


# %%
condicion = (panama["MARCA"].isna()) & (panama["SEGMENTO.1"].notna())
panama[condicion]


# %%
panama.info()
# %%
