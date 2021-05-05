#xgboost
from sys import argv
from xgboost import XGBRegressor
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# scriptname, dataset2load = argv
# if dataset2load ==
data = pd.read_csv('dataset_finale_miRNa.csv', index_col=[0])
target = []
X1 = data.values  # matrice con solo i valori numerici
Y1 = list(data.axes[0])  # target dei 'tumori' (tipologia)
for line in Y1:
    line = line.strip('"(').strip("',)")
    target.append(line)  # rimuovo caratteri in eccesso

# integer encode
# Ho bisogno di trasformare il target da caratteri a numeri, nel random forest viene fatto da pd.getdummies per linear regression
# utilizzo integer encoder
label_encoder = LabelEncoder()
target_i = label_encoder.fit_transform(target)  # target integer encoded
names1 = np.array(data.axes[1]) #nomi delle features (geni)




# define the model
XGB = XGBRegressor()
# fit the model
XGB.fit(X1, target_i)
# get importance
#importance = model.feature_importances_
# summarize feature importance
# print( "XGBoost features sorted by their score:")
# print( sorted(zip(map(lambda x: round(x, 4), XGB.feature_importances_), names1),reverse=True))
f = open('Result_FS.txt','a')
f.write("\nXGBoost features sorted by their score:\n")
feat_xgb = sorted(zip(map(lambda x: round(x, 4), XGB.feature_importances_), names1),reverse=True)
f.write(str(feat_xgb[0:20]))
f.close()
print('end')
