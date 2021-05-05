import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
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
model = LinearRegression()
# fit the model
model.fit(X1, target_i)
# get importance
importance = model.coef_
# summarize feature importance
f = open('Result_FS.txt','a')
f.write("\nLinear regression features sorted by their score:\n")
feat_lr = sorted(zip(map(lambda x: round(x, 4), importance), names1),reverse=True)
f.write(str(feat_lr[0:20]))
f.close()
# print( "Linear regression features sorted by their score:")
# print( sorted(zip(map(lambda x: round(x, 4), importance), names1),reverse=True))
# for i,v in enumerate(importance):
# 	print('Feature: %0d, Score: %.5f' % (i,v))
# # plot feature importance
# pyplot.bar([x for x in range(len(importance))], importance)
# pyplot.show()
print('end')
