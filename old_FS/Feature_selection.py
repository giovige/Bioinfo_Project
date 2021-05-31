#FEATURE SELECTION TRAMITE RANDOM FOREST E LINEAR REGRESSION
#Note: eliminare a priori le feature con tutti e quasi tutti i valori zero nel dataset a priori
import pandas as pd
import numpy as np
from numpy import array
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestRegressor
import numpy as np
from matplotlib import pyplot


#Import data
data = pd.read_csv('scaled_dataset_finale_miRNA.csv', index_col=[0])
names1 = np.array(data.axes[1]) #nomi delle features (geni)


target = []
X1 = data.values #matrice con solo i valori numerici
Y1 = list(data.axes[0]) #target dei 'tumori' (tipologia)
for line in Y1:
    line = line.strip('"(').strip("',)")
    target.append(line) #rimuovo caratteri in eccesso

# integer encode
#Ho bisogno di trasformare il target da caratteri a numeri, nel random forest viene fatto da pd.getdummies per linear regression
#utilizzo integer encoder
label_encoder = LabelEncoder()
target_i= label_encoder.fit_transform(target) #target integer encoded

target_b = pd.get_dummies(target) # random forest non accetta come input il target sotto forma di caratteri per questo utilizzo pdgetdummies


# #RFECV
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV
from sklearn.datasets import make_classification

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

print("Optimal number of features : %d" % rfecv.n_features_)


support = rfecv.get_support()
idx =np.where(support)[0] #indici dove support è True
f = open('Result_FS.txt','a+')
f.write("\nRFECV features:\n")
f.write(str(names1[idx]))
f.close()

optimal_features = X1[:, rfecv.support_]

n = 100 # to select top n features
feature_ranks = rfecv.ranking_
feature_ranks_with_idx = enumerate(feature_ranks)
sorted_ranks_with_idx = sorted(feature_ranks_with_idx, key=lambda x: x[1])
top_n_idx = [idx for idx, rnk in sorted_ranks_with_idx[:n]]

top_n_features = names1[top_n_idx]

f = open('Result_RFEcv.txt','a+')
f.write("\nRFECV features sorted by their score:\n")

f.write(str(top_n_features))
f.close()
