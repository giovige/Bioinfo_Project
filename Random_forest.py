# RANDOM FOREST
import pandas as pd
import numpy as np
from numpy import array
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# Import data
data = pd.read_csv('dataset_finale_miRNa.csv', index_col=[0])
names1 = np.array(data.axes[1])  # nomi delle features (geni)

# ## Random Forest mean decrease impurity
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

target_b = pd.get_dummies(target)  # random forest non accetta come input il target sotto forma di caratteri per questo utilizzo pdgetdummies

rf = RandomForestRegressor()
rf.fit(X1, target_i)
# print( "Random Forest features sorted by their score:")
# print( sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names1),reverse=True)) #stampo in ordine le features
f = open('Result_FS.txt', 'a')
feat_rf = sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names1), reverse=True)
f.write("Random Forest features sorted by their score:\n")
f.write(str(feat_rf[0:20]))
f.close()
print('end')
