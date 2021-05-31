# RANDOM FOREST
from sklearn.ensemble import RandomForestRegressor
from n4_featureSelectionMethods.common_functions import read_dataset, get_param, wrong_parameters


def random_forest(datasetFile, labelDim, tosave):
    print('\nUsing ' + datasetFile)

    data, X1, target_i, names1 = read_dataset(datasetFile, labelDim)

    rf = RandomForestRegressor()
    rf.fit(X1, target_i)

    print('opening file...')    # saving most relevant feature for this FS method
    f = open('Result_FS.txt', 'a')
    feat_rf = sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names1), reverse=True)
    f.write("Random Forest features sorted by their score:\n")
    f.write(str(feat_rf[0:20]))
    f.close()
    print('end')

    if tosave == 'y':
        print('saving new dataset...')
        best_feature = data[feat_rf]
        final_dataset_name = 'RF_' + labelDim + '_' + dataType + 'RNA.csv'
        best_feature.to_csv(final_dataset_name, encoding='utf-8')
    else:
        print('End. Dataset not saved.')


labelType, dataType, saveData = get_param()
if wrong_parameters(labelType, dataType, saveData):     # verifico input utente
    exit(-1)
datasetName = 'dataset_finale_' + dataType + 'RNA.csv'
random_forest(datasetName, labelType, saveData)