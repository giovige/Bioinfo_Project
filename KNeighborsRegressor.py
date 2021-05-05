## KNeighborsRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.inspection import permutation_importance
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


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
KN = KNeighborsRegressor()
# fit the model
KN.fit(X1, target_i)
# perform permutation importance
results = permutation_importance(KN, X1, target_i, scoring='neg_mean_squared_error')
# get importance
# importance = results.importances_mean
# summarize feature importance
# print( "KNeighborsRegressor features sorted by their score:")
# print( sorted(zip(map(lambda x: round(x, 4), results.importances_mean), names1),reverse=True))
f = open('Result_FS.txt', 'a')
f.write("\nKNeighborsRegressor features sorted by their score:\n")
feat_kn= sorted(zip(map(lambda x: round(x, 4), results.importances_mean), names1),reverse=True)
f.write(str(feat_kn[0:20]))
f.close()
print('end')
