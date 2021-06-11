# #RFECV
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from n4_featureSelectionMethods.common_functions import read_dataset, get_param, wrong_parameters, subset_dataset


def rfe_cv(datasetFile, labelDim, tosave, n):
    print('\nUsing ' + datasetFile)

    data, X1, target_i, names1 = read_dataset(datasetFile, labelDim)


    # Create the RFE object and compute a cross-validated score.
    svc = SVC(kernel="linear")
    # The "accuracy" scoring is proportional to the number of correct
    # classifications

    min_features_to_select = 1  # Minimum number of features to consider
    rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(2),
                  scoring='accuracy',
                  min_features_to_select=min_features_to_select)
    print('Running RFECV')
    rfecv.fit(X1, target_i)

    n = 100  # to select top n features
    feature_ranks = rfecv.ranking_
    feature_ranks_with_idx = enumerate(feature_ranks)
    sorted_ranks_with_idx = sorted(feature_ranks_with_idx, key=lambda x: x[1])
    top_n_idx = [idx for idx, rnk in sorted_ranks_with_idx[:n]]
    top_n_features = names1[top_n_idx]

    f = open('Result_FS.txt', 'a+')
    f.write("\nRFECV features sorted by their score:\n")
    f.write(str(top_n_features))
    f.close()

    if tosave == 'y':
        print('saving new dataset...')
        final_dataset_name = 'RFEcv_' + str(n) + '_' + labelDim + '_' + dataType + 'RNA.csv'
        best_feature_dataset = subset_dataset(data, sorted_ranks_with_idx, n)
        best_feature_dataset.to_csv(final_dataset_name, encoding='utf-8')
    else:
        print('End. Dataset not saved.')


labelType, dataType, saveData, nfeatures = get_param()
if wrong_parameters(labelType, dataType, saveData, nfeatures):     # verifico input utente
    exit(-1)
datasetName = 'dataset_finale_' + dataType + 'RNA.csv'
rfe_cv(datasetName, labelType, saveData, nfeatures)
