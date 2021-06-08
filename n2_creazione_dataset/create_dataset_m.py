import gzip
import os
import pandas as pd

f = open('new_label_m.txt', 'r')
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
yourpath = os.path.join(yourpath, os.pardir) + "\mRNA"

dataset = {}
tip = []
for root, dirs, files in os.walk(yourpath, topdown=False):
    ciao = 1

print('\nlettura file mRNA')
os.chdir(yourpath)
for lb in label.items():
    if lb[0] in files:  # se il file del label esiste nella cartella di mrna/mirna
        num_classes += 1
        tip.append(lb[1])  # tip = elenco labels (classi tumori)
        file = lb[0]
        f = gzip.open(file, "rb")
        lines = f.readlines()
        for line in lines:
            line = str(line)
            line = line.split('\\')
            gene = line[0].strip("b'")
            value = line[1].strip('t')
            if gene in dataset:
                dataset[gene].append(value)
            else:
                dataset[gene] = []  # inizializza lista relativa ad ogni singolo gene (= colonna)
                dataset[gene].append(value)

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
finale.to_csv('dataset_mRNA.csv', encoding='utf-8')  # Salvataggio matrice finale
print('\n' + str(num_classes) + ' campioni presenti')
print('\nfine scrittura csv m_RNA')

