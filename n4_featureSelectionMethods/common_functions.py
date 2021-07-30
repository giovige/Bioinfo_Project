from sklearn.preprocessing import LabelEncoder
import numpy as np
import pandas as pd
# # library with functions called by multiple FS scripts # - read_dataset(datasetName, labelDimentionality) --> reads
#                                   a csv file, saving the dataset in a dataframe, using some/all type of class labels
# - get_param() --> requests to user: type of label to use, input dataset to read, number of feature to select
# - wrong_parameters(labelType, saveData, n) --> check if parameters inserted by user are valid
# - subset_dataset(dataset, bestfeatures, n) --> takes a dataset, subsetting it with the list of features taken as input

def read_dataset(datasetName, labelDimentionality):
    data = pd.read_csv(datasetName, index_col=[0])
    target = []
    X1 = data.values
    Y1 = list(data.axes[0])

    if labelDimentionality == 'c':
        for line in Y1:
            line = line.strip('"(').strip("',)")
            target.append(line)
    #Change label names for reduced label
    else:
        for line in Y1:
            line = line.strip('"(').strip("',)")
            if 'TCGA' in line:
                line = 'TGCA'
            if 'TARGET' in line:
                line = 'TARGET'
            if 'CPTAC' in line:
                line = 'CPTAC-3'
            target.append(line)

    # integer encode
    label_encoder = LabelEncoder()
    target_i = label_encoder.fit_transform(target)  # target integer encoded
    features = np.array(data.axes[1])  # nomi delle features (geni)

    return data, X1, target_i, features


def get_param():
    labelType = input('> Complete or reduced list of labels? (R = reduced/C = complete)').lower()
    dataType = input('> Which dataset do you want to process?')
    saveData = input('> Do you want to save the dataset containing only the most relevant features? (Y/N)').lower()
    n = int(input('> How many features do you want to select? '))
    return labelType, dataType, saveData, n


def wrong_parameters(labelType, saveData, n):
    return (saveData != 'y' and saveData != 'n') or (labelType != 'r' and labelType != 'c') or (n < 1 or n > 1000)


def subset_dataset(dataset, bestfeatures, n):   # riduce 'dataset' prendendo solo le feature presenti in 'bestfeatures'
    feat_names = []
    for f in bestfeatures:
        feat_names.append(f[1])
    new_dataset = dataset[feat_names[0:n]]
    return new_dataset
