## Decision tree
from sklearn.tree import DecisionTreeRegressor
from n4_featureSelectionMethods.common_functions import read_dataset, get_param, wrong_parameters, subset_dataset


def decision_tree(datasetFile, labelDim, tosave, n):
    print('\nUsing ' + datasetFile)

    data, X1, target_i, names1 = read_dataset(datasetFile, labelDim)

    # define the model
    DCT = DecisionTreeRegressor()
    # fit the model
    DCT.fit(X1, target_i)

    f = open('Result_FS.txt', 'a')
    f.write("\nDecision tree features sorted by their score:\n")
    feat_dct = sorted(zip(map(lambda x: round(x, 4), DCT.feature_importances_), names1), reverse=True) #sort the selected features with score and name
    f.write(str(feat_dct[0:n]))
    f.close()
    print('end')

    if tosave == 'y':
        print('saving new dataset...')
        # geneType = str(datasetFile).split('_')[2].split('.')[0]
        final_dataset_name = 'DecTree_' + str(n) + '_' + labelDim + '_' + dataType
        best_feature_dataset = subset_dataset(data, feat_dct, n)
        best_feature_dataset.to_csv(final_dataset_name, encoding='utf-8') #new dataset wit best features
    else:
        print('End. Dataset not saved.')


labelType, dataType, saveData, nfeatures = get_param()
if wrong_parameters(labelType, saveData, nfeatures):     # verify input user
    exit(-1)
datasetName = dataType
decision_tree(datasetName, labelType, saveData, nfeatures)
