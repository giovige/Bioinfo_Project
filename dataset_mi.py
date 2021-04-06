import os
import tempfile

import pandas as pd
import numpy as np

f = open('label_miRNA.txt', 'r')
label = {}
lb = f.readline()
print('main data_mi()')
while lb:
    l = lb.split(':')
    label[l[0]] = []
    label[l[0]].append(l[1].strip("[\'").strip("\'] \n"))
    lb = f.readline()

f.close()

final_file_path = os.getcwd()
yourpath = os.getcwd() + "\miRNA"
cont = 0
dataset = {}
tip = []
for root, dirs, files in os.walk(yourpath, topdown=False):
    ciao = 1

for name in dirs:
    if name == dirs[0]:
        os.chdir(os.path.join(root, name))
        arr = os.listdir()
        for file in arr:
            if file in label:
                # if len(file)> 16:
                tip.append(label[file])
                f = open(file, 'r')
                lines = f.readlines()
                for line in lines:
                    if line[0] == 'h':
                        alfio = line.split('\t')
                        # dataset[str(label[file])]=[]
                        # dataset[str(label[file])].append(alfio[2])
                        dataset[alfio[0]] = []
                        dataset[alfio[0]].append(alfio[2])


    else:
        os.chdir(os.path.join(root, name))
        arr = os.listdir()
        for file in arr:
            if file in label:
                tip.append(label[file])
                f = open(file, 'r')
                lines = f.readlines()
                for line in lines:
                    if line[0] == 'h':
                        alfio = line.split('\t')
                        dataset[alfio[0]].append(alfio[2])
                        # dataset[str(label[file])].append(alfio[2])


# Creo il dataset finale utilizzando pandas
tip = pd.DataFrame(tip)
finale = pd.DataFrame(index=tip,
                      columns=dataset.keys())  # Creo una matrice con i nomi delle colonne le tipologie di tumori
# e come righe i nomi dei geni
dataset1 = pd.Series(dataset)
a = dataset1.axes[0]  # lista indici

for index in a:
    if index in finale:
        finale[index] = dataset1[index]

os.chdir(final_file_path)
finale.to_csv('dataset_finale_miRNA.csv', encoding='utf-8')  # Salvataggio matrice finale
print('\nfine scrittura csv mi_RNA')