import pandas as pd
import numpy as np
import rcca


# -----------------------CCA
def cca_fs(m_data, mi_data, save):
    values_m = m_data.values
    values_mi = mi_data.values
    names_m_ft = np.array(m_data.axes[1])
    names_mi_ft = np.array(mi_data.axes[1])
    # CCACrossValidate permits to o estimate hyperparameters empirically by using grid search with cross-validation.
    # cca_cross = rcca.CCACrossValidate(kernelcca=True, ktype='gaussian', regs=[1e-3, 1e-2, 1e-1], numCCs=[2, 10, 20])
    # cca_cross.train([values_m, values_mi])
    # the best performances have been found with reg = 0.1 and numCC = 10

    cca = rcca.CCA(kernelcca=True, ktype='gaussian', reg=0.1, numCC=10)
    cca.train([values_m, values_mi])

    # Canonical weights
    W1 = cca.ws[0]
    W2 = cca.ws[1]

    W1 = pd.DataFrame(W1)
    # Compute the normalized weights matrix
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

    # Order the most important 50 features
    top_50_mft = []
    sorted_m_ft = sorted(zip(map(lambda x: x, score1), names_m_ft), reverse=True)
    for i in range(50):
        top_50_mft.append(sorted_m_ft[i][1])
    top_50_m_data = m_data[top_50_mft]

    top_50_mift = []
    sorted_mi_ft = sorted(zip(map(lambda x: x, score2), names_mi_ft), reverse=True)
    for i in range(50):
        top_50_mift.append(sorted_mi_ft[i][1])
    top_50_mi_data = mi_data[top_50_mift]

    CCA_result_dataset = pd.concat([top_50_m_data, top_50_mi_data],
                                   axis=1)  # new dataset composed by top 50 mRNA and miRNA ft
    if save == 1:
        CCA_result_dataset.to_csv('CCA_result_dataset.csv')
    return CCA_result_dataset, top_50_mft, top_50_mift

# m_data = pd.read_csv('scaled_dataset_finale_mRNA.csv', index_col=[0])
# mi_data = pd.read_csv('scaled_dataset_finale_miRNA.csv', index_col=[0])
# [data, mRNA_ft, miRNA_ft] = cca_fs(m_data,mi_data,0)
