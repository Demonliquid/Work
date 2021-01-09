# %%
from PIL import Image
import pytesseract
import re
import pandas
import csv
import os
from numpy import loadtxt
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# %%
directory = r'C:\Users\Martin96\Desktop\Laburo\Registros'
for foto in os.listdir(directory):
        if foto.endswith(".jpg"):
            img = Image.open(foto)
            text = pytesseract.image_to_string(img, lang="spa")


            