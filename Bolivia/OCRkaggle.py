#%%
# Generic Libraries
from PIL import Image
import os
import pandas as pd
import numpy as np
import re,string,unicodedata

#Tesseract Library
import pytesseract

#Warnings
import warnings
warnings.filterwarnings("ignore")

#Garbage Collection
import gc

#Gensim Library for Text Processing
import gensim.parsing.preprocessing as gsp
from gensim import utils

#TextBlob Library (Sentiment Analysis)
from textblob import TextBlob, Word

#Plotting Libraries
import matplotlib.pyplot as plt
import seaborn as sns


# %%
sample_images = r'C:\Users\Martin96\Desktop\Laburo\Registros'

ex_txt = []

processes = [
               gsp.strip_tags, 
               gsp.strip_punctuation,
               gsp.strip_multiple_whitespaces,
               gsp.strip_numeric,
               gsp.remove_stopwords, 
               gsp.strip_short, 
               gsp.stem_text
            ]

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# %%
def traverse(directory):
    path, dirs, files = next(os.walk(directory))
    fol_nm = os.path.split(os.path.dirname(path))[-1]
    print(f'Number of files found in "{fol_nm}" : ',len(files))


def TxtExtract(directory):
    """
    This function will handle the core OCR processing of images.
    """
    
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filepath = subdir + os.sep + file
            text = pytesseract.image_to_string(Image.open(filepath), timeout=5)
            if not text:
                ex_txt.extend([[file, "blank"]])
            else:   
                ex_txt.extend([[file, text]])
                
    fol_nm = os.path.split(os.path.dirname(subdir))[-1]
    
    print(f"Text Extracted from the files in '{fol_nm}' folder & saved to list..")


def proc_txt(txt):
    text = txt.lower()
    text = utils.to_unicode(text)
    for p in processes:
        text = p(text)
    return text


# %%
traverse(sample_images)


# %%
TxtExtract(sample_images)


# %%
ext_df = pd.DataFrame(ex_txt,columns=['FileName','Text'])

# %%
ext_df['Text_Pr'] = ext_df['Text'].apply(lambda x: proc_txt(x))


# %%
ext_df_txt = ext_df[(  ext_df['Text_Pr'] != 'blank'  )]
