import os
import pandas as pd
import numpy as np
import gzip
from zipfile import ZipFile

f = open('label_mRNA.txt', 'r')
label = {}
lb = f.readline()
print('main()')
while lb:
    l = lb.split(':')
    label[l[0]] = []
    label[l[0]].append(l[1].strip("[\'").strip("\'] \n"))
    lb = f.readline()
f.close()

# yourpath = r'C:\Users\giuli\Desktop\MAGISTRALE\ultimo semestre\Bioinformatica\progetto\Dati\mRNA'
final_file_path = os.getcwd()
yourpath = os.getcwd() + "\mRNA"
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
                tip.append(label[file])
                a_file = gzip.open(file, "rb")
                # lines = a_file.readlines()
                # for i in range(len(lines)):
                #     line = lines[i]
                #     line = str(line)
                #     line = line.split('\\')
                #     gene = line[0].strip("b'")
                #     value = line[1].strip('t')
                #     dataset[gene] = []
                #     dataset[gene].append(value)
                line = a_file.readline()
                while line:
                    line = str(line)
                    line = line.split('\\')
                    gene = line[0].strip("b'")
                    value = line[1].strip('t')
                    dataset[gene] = []
                    dataset[gene].append(value)
                    line = a_file.readline()
                a_file.close()
                # for line in lines:
                #     if line[0] == 'E':
                #         alfio = line.split('\t')
                #         dataset[alfio[0]] = []
                #         dataset[alfio[0]].append(alfio[1])

    else:
        os.chdir(os.path.join(root, name))
        arr = os.listdir()
        for file in arr:
            if file in label:
                tip.append(label[file])
                a_file = gzip.open(file, "rb")
                # lines = a_file.readlines()
                # for i in range(len(lines)):
                #     line = lines[i]
                #     line = str(line)
                #     line = line.split('\\')
                #     gene = line[0].strip("b'")
                #     value = line[1].strip('t')
                #     dataset[gene].append(value)
                line = a_file.readline()
                while line:
                    line = str(line)
                    line = line.split('\\')
                    gene = line[0].strip("b'")
                    value = line[1].strip('t')
                    dataset[gene].append(value)
                    line = a_file.readline()
                a_file.close()
                # f = open(file, 'r')
                # lines = f.readlines()
                # for line in lines:
                #     if line[0] == 'h':
                #         alfio = line.split('\t')
                #         dataset[alfio[0]].append(alfio[2])
                #         #dataset[str(label[file])].append(alfio[2])

# #Costruisco il dataset finale con la libreria numpy
# finale1 = np.zeros((len(tip)+1,len(dataset.keys())+1)).astype(np.str) #matrice vuota
# #Inserisco la tipologia dei tumori nella prima colonna
# i = 1
# for name in tip:
#     finale1[i,0] = name[0]
#     i += 1
# #Inserisco i nomi dei geni nella prima riga e riempio le colonne
# i = 1
# for keys in dataset.keys():
#     finale1[0,i] = keys
#     finale1[1:,i] = dataset[keys]
#     i += 1
# #Salvo il dataset finale
# f = open('finale1_mrna.txt','w+')
# for k in range(len(tip)+1):
#     f.write(str(finale1[k,:]))
# f.close()
#
# zipObj = ZipFile('sample.zip', 'w')
# zipObj.write(finale1)
# zipObj.close()

# finale1 = pd.DataFrame(finale1)
# finale1.to_csv('dataset_finale1_miRNa.csv')  # Salvataggio matrice finale
#
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
finale.to_csv('dataset_finale_mRNA.csv', encoding='utf-8')  # Salvataggio matrice finale
print('\nfine scrittura csv m_RNA')