#xgboost
from xgboost import XGBRegressor
from n4_featureSelectionMethods.common_functions import read_dataset, get_param, wrong_parameters


def XG_Boost(datasetFile, labelDim, tosave):
    print('\nUsing ' + datasetFile)

    data, X1, target_i, names1 = read_dataset(datasetFile, labelDim)

    # define the model
    XGB = XGBRegressor()
    # fit the model
    XGB.fit(X1, target_i)

    f = open('Result_FS.txt', 'a')
    f.write("\nXGBoost features sorted by their score:\n")
    feat_xgb = sorted(zip(map(lambda x: round(x, 4), XGB.feature_importances_), names1),reverse=True)
    f.write(str(feat_xgb[0:20]))
    f.close()
    print('end')

    if tosave == 'y':
        print('saving new dataset...')
        best_feature = data[feat_xgb]
        final_dataset_name = 'XGB_' + labelDim + '_' + dataType + 'RNA.csv'
        best_feature.to_csv(final_dataset_name, encoding='utf-8')
    else:
        print('End. Dataset not saved.')


labelType, dataType, saveData = get_param()
if wrong_parameters(labelType, dataType, saveData):     # verifico input utente
    exit(-1)
datasetName = 'dataset_finale_' + dataType + 'RNA.csv'
XG_Boost(datasetName, labelType, saveData)