import os
import pandas as pd

f = open('label_mi.txt', 'r')
label = {}
lb = f.readline()
print('reading_label()')
while lb:
    l = lb.split(':')
    label[l[0]] = []
    label[l[0]].append(l[1].strip("[[\'").strip("\']] \n"))
    lb = f.readline()
f.close()

num_classes = 0
yourpath = os.getcwd()
final_file_path = os.path.join(yourpath, os.pardir)
yourpath = os.path.join(yourpath, os.pardir) + "\miRNA"

dataset = {}
tip = []
for root, dirs, files in os.walk(yourpath, topdown=False):
    ciao = 1

print('\nlettura file miRNA')
os.chdir(yourpath)
for lb in label.items():
    if lb[0] in files:  # se il file del label esiste nella cartella di mrna/mirna
        num_classes += 1
        tip.append(lb[1])  # tip = elenco labels (classi tumori)
        file = lb[0]
        f = open(file, 'r')
        lines = f.readlines()
        for line in lines:
            if line[0] == 'h':  # ogni gene inizia per h: es. 'hsa-54'
                geneRow = line.split('\t')  # contiene riga parsificata di un file mirna/mrna, dove riga[0] è il nome del gene
                if geneRow[0] in dataset:
                    dataset[geneRow[0]].append(geneRow[2])
                else:
                    dataset[geneRow[0]] = []  # inizializza lista relativa ad ogni singolo gene (= colonna)
                    dataset[geneRow[0]].append(geneRow[2])
f.close()
print(num_classes)
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
finale.to_csv('dataset_miRNA.csv', encoding='utf-8')  # Salvataggio matrice finale
print('\n' + str(num_classes) + ' campioni presenti')
print('\nfine scrittura csv mi_RNA')

