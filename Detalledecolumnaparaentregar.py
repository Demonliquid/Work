# %%
import csv
my_dict = dict(base["SEGMENTO.1"].value_counts())

with open(r'D:\Basededatos\SEGMENTO1.csv', 'w') as output:
    writer = csv.writer(output)
    for key, value in my_dict.items():
        writer.writerow([key, value])
