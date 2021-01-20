# %%
import os
import pandas as pd
import numpy as np
import datetime


# %%
datosVM = pd.read_csv(r'D:\Basededatos\datos_VM_20.09.20.txt', sep="|", header=None)

# %%
datosVM.columns = ["PATENTE",
                   "SEGMENTO.1",
                   "MODELO",
                   "VERSION (SALES DESCRIPTION)",
                   "RUT",
                   "NUMERO MOTOR",
                   "AÑO",
                   "NOMBRE",
                   "CANTIDAD"
                   ]
datosVM = datosVM[["PATENTE", "SEGMENTO.1", "MODELO", "VERSION (SALES DESCRIPTION)", "RUT", "NUMERO MOTOR", "AÑO"]]


# %%
datosVM.to_csv(r'D:\Basededatos\Limpioparaentregar\Chile BBDD\datosVM.csv', index=False)

# %%
