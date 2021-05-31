from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd


def read_dataset(datasetName, labelDimentionality):
    data = pd.read_csv(datasetName, index_col=[0])
    target = []
    X1 = data.values  # matrice con solo i valori numerici
    Y1 = list(data.axes[0])  # target dei 'tumori' (tipologia)

    if labelDimentionality == 'c':      # label completo
        for line in Y1:
            line = line.strip('"(').strip("',)")
            target.append(line)  # rimuovo caratteri in eccesso
    else:   # label ridotto
        for line in Y1:
            line = line.strip('"(').strip("',)")
            if 'TCGA' in line:
                line = 'TGCA'
            if 'TARGET' in line:
                line = 'TARGET'
            if 'CPTAC' in line:
                line = 'CPTAC-3'
            target.append(line)  # rimuovo caratteri in eccesso

    # integer encode
    # Ho bisogno di trasformare il target da caratteri a numeri
    label_encoder = LabelEncoder()
    target_i = label_encoder.fit_transform(target)  # target integer encoded
    features = np.array(data.axes[1])  # nomi delle features (geni)

    return data, X1, target_i, features


def get_param():
    labelType = input('> Complete or reduced list of labels? (R = reduced/C = complete)').lower()
    dataType = input('> Which dataset do you want to process?(mi= miRNA/m = mRNA)').lower()
    saveData = input('> Do you want to save the dataset containing only the most relevant features? (Y/N)').lower()
    return labelType, dataType, saveData


def wrong_parameters(labelType, dataType, saveData):
    return (saveData != 'y' and saveData != 'n') or (labelType != 'r' and labelType != 'c') or (dataType != 'm' and dataType != 'mi')
