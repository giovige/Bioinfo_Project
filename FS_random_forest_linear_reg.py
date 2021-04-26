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
data = pd.read_csv('dataset_finale_miRNa.csv', index_col=[0])

## Random Forest mean decrease impurity
target = []
X1 = data.values #matrice con solo i valori numerici
Y1 = list(data.axes[0]) #target dei 'tumori' (tipologia)
for line in Y1:
    line = line.strip('"(').strip("',)")
    target.append(line) #rimuovo caratteri in eccesso
target_b = pd.get_dummies(target) # random forest non accetta come input il target sotto forma di caratteri per questo utilizzo pdgetdummies
names1 = np.array(data.axes[1]) #nomi delle features (geni)
rf = RandomForestRegressor()
rf.fit(X1,target_b)
print( "Random Forest features sorted by their score:")
print( sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names1),reverse=True)) #stampo in ordine le features

## Stability selection

# integer encode
#Ho bisogno di trasformare il target da caratteri a numeri, nel random forest viene fatto da pd.getdummies per linear regression
#utilizzo integer encoder
label_encoder = LabelEncoder()
target_i= label_encoder.fit_transform(target) #target integer encoded

## Linear regression
from sklearn.linear_model import LinearRegression
# define the model
model = LinearRegression()
# fit the model
model.fit(data, target_i)
# get importance
importance = model.coef_
# summarize feature importance
print( "Linear regression features sorted by their score:")
print( sorted(zip(map(lambda x: round(x, 4), importance), names1),reverse=True))
# for i,v in enumerate(importance):
# 	print('Feature: %0d, Score: %.5f' % (i,v))
# # plot feature importance
# pyplot.bar([x for x in range(len(importance))], importance)
# pyplot.show()
