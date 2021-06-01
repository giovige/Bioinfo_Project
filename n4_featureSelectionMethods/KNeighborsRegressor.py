## KNeighborsRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.inspection import permutation_importance
from n4_featureSelectionMethods.common_functions import read_dataset, get_param, wrong_parameters, subset_dataset


def KNeighborsReg(datasetFile, labelDim, tosave, n):
    print('\nUsing ' + datasetFile)

    data, X1, target_i, names1 = read_dataset(datasetFile, labelDim)

    # define the model
    KN = KNeighborsRegressor()
    # fit the model
    print('KN.fit()')
    KN.fit(X1, target_i)
    # perform permutation importance
    results = permutation_importance(KN, X1, target_i, scoring='neg_mean_squared_error')

    print('opening file...')    # saving most relevant feature for this FS method
    f = open('Result_FS.txt', 'a')
    f.write("\nKNeighborsRegressor features sorted by their score:\n")
    feat_kn = sorted(zip(map(lambda x: round(x, 4), results.importances_mean), names1), reverse=True)
    f.write(str(feat_kn[0:20]))
    f.close()

    if tosave == 'y':
        print('saving new dataset...')
        final_dataset_name = 'KN_' + str(n) + '_' + labelDim + '_' + dataType + 'RNA.csv'
        best_feature_dataset = subset_dataset(data, feat_kn, n)
        best_feature_dataset.to_csv(final_dataset_name, encoding='utf-8')
    else:
        print('End. Dataset not saved.')


labelType, dataType, saveData, nfeatures = get_param()
if wrong_parameters(labelType, dataType, saveData):     # verifico input utente
    exit(-1)
datasetName = 'dataset_finale_' + dataType + 'RNA.csv'
KNeighborsReg(datasetName, labelType, saveData, nfeatures)
