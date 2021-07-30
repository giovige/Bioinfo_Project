import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sys import argv

#'dataset_Preprocessing.py' do the pre-processing for the dataset. In particular:
# -delete features with less than n values (considered non informative)
# -zero mean rescale
# -min max rescale

print("Main()")
scriptname, dataset_name = argv
todelete_filename = 'zerovalue20.txt'
# dataset_name = 'dataset_miRNA.csv'

# Select the names for delete the features (otherwise comment)
# worstFeatures = []
# f = open(todelete_filename, 'r') # file with columns (features) to delete
# line = f.readline()
# while line:
#     line = line.strip().split('\n')[0]  # remove '\n' from name columns
#     worstFeatures.append(line)
#     line = f.readline()
# f.close()
# -------------------------------------------------------------------


# LOAD DATASET
m_data = pd.read_csv(dataset_name, index_col=[0])
m_names = np.array(m_data.axes[1])  # nomi delle features (geni)

# Delete features with less than n values
n = 20  # numero di valori
worstFeatures = []
j = 0
for i in m_names:
    cont = 0
    for v in m_data[i]:
        if v != 0:
            cont += 1
    if cont < n:
        worstFeatures.append(i)
        j += 1
print(j)
# ------------------------------------------

j = 0
for i in range(0, len(worstFeatures)):
    m_data.pop(worstFeatures[i])
    j += 1
print('\nEliminate ' + str(j) + ' feature da ' + dataset_name)
# m_data.pop(line)

# Zero mean rescale
zero_mean_scaler = preprocessing.StandardScaler()
dataset_mean = zero_mean_scaler.fit(m_data.values).transform(m_data.values)

# MinMAx rescale
minmax_scaler = MinMaxScaler()
dataset_minmax = minmax_scaler.fit(dataset_mean).transform(dataset_mean)

scaled_dataset = pd.DataFrame(dataset_minmax, index=m_data.index, columns=m_data.columns)

# Data saving
newFileName = 'scaled_' + dataset_name
scaled_dataset.to_csv(newFileName, encoding='utf-8')  # Salvataggio matrice finale
print('File salvato correttamente!')
