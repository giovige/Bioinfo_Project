# #RFECV
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold
from sklearn.feature_selection import RFECV


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


# Create the RFE object and compute a cross-validated score.
svc = SVC(kernel="linear")
# The "accuracy" scoring is proportional to the number of correct
# classifications

min_features_to_select = 1  # Minimum number of features to consider
rfecv = RFECV(estimator=svc, step=1, cv=StratifiedKFold(2),
              scoring='accuracy',
              min_features_to_select=min_features_to_select)
rfecv.fit(X1, target_i)

print("Optimal number of features : %d" % rfecv.n_features_)

# Plot number of features VS. cross-validation scores
plt.figure()
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.plot(range(min_features_to_select,
               len(rfecv.grid_scores_) + min_features_to_select),
         rfecv.grid_scores_)
plt.show()

support = rfecv.get_support()
idx =np.where(support)[0]   # indici dove support è True
f = open('Result_FS.txt', 'a+')
f.write("\nRFECV features:\n")
f.write(str(names1[idx]))
f.close()
print('end')
