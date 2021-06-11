import pandas as pd
import numpy as np
import rcca
from sklearn.preprocessing import LabelBinarizer
from numpy import array

"""
'cca_fs' is a function that selecet the best features of each dataset compute the canonical correlation analysis
In particulare given the datasets as input, the function computes the score for each features stariting from
the weight matrix produced by cca. It is also possible to give as imput the label of the samples to do
'supervised' cca.
Input:
two datasets (m_data, mi_data)
n: number of features to select from each dataset
save : 1 if you want to save the final dataset
label: to perform 'supervised' CCA give the label of the samples
Output:
Dataset: the final dataset with the top n features from each input dataset
mRNA_ft : list of top n mRNA features
miRNA_ft : list of top n miRNA features

"""


##-----------------------CCA
def cca_fs(m_data, mi_data, n, label, save):
    values_m = m_data.values
    values_mi = mi_data.values
    names_m_ft = np.array(m_data.axes[1])
    names_mi_ft = np.array(mi_data.axes[1])
    # CCACrossValidate permits to o estimate hyperparameters empirically by using grid search with cross-validation.
    # cca_cross = rcca.CCACrossValidate(kernelcca=True, ktype='gaussian', regs=[1e-3, 1e-2, 1e-1], numCCs=[2, 10, 20])
    # cca_cross.train([values_m, values_mi])
    # cca_cross.train([values_m, values_mi,label])
    # To tune hyperparamenters reg and numCC use rcca.crossvalidate to obtain the best values.
    # If the hyperparameters are already tuned use rcca.CCA

    # In our case we obtain the best results with reg = 0.1 numCC = 10
    cca = rcca.CCA(kernelcca=True, ktype='gaussian', reg=0.1, numCC=10)

    if label is False:
        cca.train([values_m, values_mi])
    else:
        label = list(m_data.axes[0])
        label = array(label)
        # Binary encode
        lb = LabelBinarizer()
        list = lb.fit_transform(label)  # Target transformed in binary encode
        cca.train([values_m, values_mi, list])

    # Canonical weights
    W1 = cca.ws[0]
    W2 = cca.ws[1]

    W1 = pd.DataFrame(W1)
    # Compute the normalized weights matrix by normalize each value for the absolute value of the sum of the column
    Q1 = np.zeros([W1.shape[0], W1.shape[1]])
    Q1 = pd.DataFrame(Q1)
    for i in range(W1.shape[1]):
        for j in range(W1.shape[0]):
            Q1[i][j] = abs(W1[i][j]) / sum(abs(W1[i]))

    # Determine the importance score for each features
    score1 = np.zeros([W1.shape[0], 1])
    for i in range(len(score1)):
        score1[i] = sum(Q1.values[i]) / Q1.values.sum()

    # Same procedures for the second weights matrix
    W2 = pd.DataFrame(W2)
    Q2 = np.zeros([W2.shape[0], W2.shape[1]])
    Q2 = pd.DataFrame(Q2)
    for i in range(W2.shape[1]):
        for j in range(W2.shape[0]):
            Q2[i][j] = abs(W2[i][j]) / sum(abs(W2[i]))

    score2 = np.zeros([W2.shape[0], 1])

    for i in range(len(score2)):
        score2[i] = sum(Q2.values[i]) / Q2.values.sum()

    # Order the most important n features
    top_mft = []
    sorted_m_ft = sorted(zip(map(lambda x: x, score1), names_m_ft), reverse=True)
    for i in range(n):
        top_mft.append(sorted_m_ft[i][1])
    top_m_data = m_data[top_mft]

    top_mift = []
    sorted_mi_ft = sorted(zip(map(lambda x: x, score2), names_mi_ft), reverse=True)
    for i in range(n):
        top_mift.append(sorted_mi_ft[i][1])
    top_mi_data = mi_data[top_mift]

    CCA_result_dataset = pd.concat([top_m_data, top_mi_data], axis=1)  # new dataset composed by top n mRNA and miRNA ft
    if save is True:
        CCA_result_dataset.to_csv('CCA_data.csv')
    return CCA_result_dataset, top_mft, top_mift


# Import Data
file1 = input('> Dataset1 = ')
file2 = input('> Dataset2 = ')
n_ft = int(input('> Number of features = '))
supervised = bool(input('> Supervised version? (1=Yes/0=No)'))
save = bool(input('> Save CCA dataset? (1=Yes/0=No)'))
m_data = pd.read_csv(file1, index_col=[0])
mi_data = pd.read_csv(file2, index_col=[0])
[data, mRNA_ft, miRNA_ft] = cca_fs(m_data, mi_data, n_ft, supervised, save)
