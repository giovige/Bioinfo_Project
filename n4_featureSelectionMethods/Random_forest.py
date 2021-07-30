# RANDOM FOREST
from sklearn.ensemble import RandomForestRegressor
from n4_featureSelectionMethods.common_functions import read_dataset, get_param, wrong_parameters, subset_dataset


def random_forest(datasetFile, labelDim, tosave, n):
    print('\nUsing ' + datasetFile)

    data, X1, target_i, names1 = read_dataset(datasetFile, labelDim)

    rf = RandomForestRegressor()
    rf.fit(X1, target_i)

    print('opening file...')    # saving most relevant feature for this FS method
    f = open('Result_FS.txt', 'a')
    feat_rf = sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names1), reverse=True)  #sort the selected features with score and name
    f.write("Random Forest features sorted by their score:\n")
    f.write(str(feat_rf[0:n]))
    f.close()
    print('end')

    if tosave == 'y':
        print('saving new dataset...')
        # geneType = str(datasetFile).split('_')[2].split('.')[0]
        final_dataset_name = 'RF_' + str(n) + '_' + labelDim + '_' + dataType
        best_feature_dataset = subset_dataset(data, feat_rf, n)
        best_feature_dataset.to_csv(final_dataset_name, encoding='utf-8') #new dataset wit best features
    else:
        print('End. Dataset not saved.')


labelType, dataType, saveData, nfeatures = get_param()
if wrong_parameters(labelType, saveData, nfeatures):     # verify input user
    exit(-1)
datasetName = dataType
random_forest(datasetName, labelType, saveData, nfeatures)
