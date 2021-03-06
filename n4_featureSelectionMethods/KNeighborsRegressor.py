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
    feat_kn = sorted(zip(map(lambda x: round(x, 4), results.importances_mean), names1), reverse=True)  #sort the selected features with score and name
    f.write(str(feat_kn[0:n]))
    f.close()

    if tosave == 'y':
        print('saving new dataset...')
        # geneType = str(datasetFile).split('_')[2].split('.')[0]
        final_dataset_name = 'KN_' + str(n) + '_' + labelDim + '_' + dataType
        best_feature_dataset = subset_dataset(data, feat_kn, n)
        best_feature_dataset.to_csv(final_dataset_name, encoding='utf-8') #new dataset wit best features
    else:
        print('End. Dataset not saved.')


labelType, dataType, saveData, nfeatures = get_param()
if wrong_parameters(labelType, saveData, nfeatures):      # verify input user
    exit(-1)
datasetName = dataType
KNeighborsReg(datasetName, labelType, saveData, nfeatures)
