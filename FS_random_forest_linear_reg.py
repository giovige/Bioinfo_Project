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

# integer encode
#Ho bisogno di trasformare il target da caratteri a numeri, nel random forest viene fatto da pd.getdummies per linear regression
#utilizzo integer encoder
label_encoder = LabelEncoder()
target_i= label_encoder.fit_transform(target) #target integer encoded

target_b = pd.get_dummies(target) # random forest non accetta come input il target sotto forma di caratteri per questo utilizzo pdgetdummies
names1 = np.array(data.axes[1]) #nomi delle features (geni)
rf = RandomForestRegressor()
rf.fit(X1,target_i)
print( "Random Forest features sorted by their score:")
print( sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names1),reverse=True)) #stampo in ordine le features

## Stability selection



## Linear regression
from sklearn.linear_model import LinearRegression
# define the model
model = LinearRegression()
# fit the model
model.fit(X1, target_i)
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

##Logistic Regression (not works)
# from sklearn.linear_model import LogisticRegression
# # define the model
# LG = LogisticRegression()
# # fit the model
# LG.fit(X1, target_i)
# # get importance
# #importance = model.coef_[0]
# # summarize feature importance
# print( "Logistic regression features sorted by their score:")
# print( sorted(zip(map(lambda x: round(x, 4), LG.coef_[0]), names1),reverse=True))

##Deision tree
from sklearn.tree import DecisionTreeRegressor
# define the model
DCT = DecisionTreeRegressor()
# fit the model
DCT.fit(X1, target_i)
# get importance
#importance = DCT.feature_importances_
# summarize feature importance
print( "Decision tree features sorted by their score:")
print( sorted(zip(map(lambda x: round(x, 4), DCT.feature_importances_), names1),reverse=True))

#xgboost
from xgboost import XGBRegressor
# define the model
XGB = XGBRegressor()
# fit the model
XGB.fit(X1, target_i)
# get importance
#importance = model.feature_importances_
# summarize feature importance
print( "XGBoost features sorted by their score:")
print( sorted(zip(map(lambda x: round(x, 4), XGB.feature_importances_), names1),reverse=True))

## KNeighborsRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.inspection import permutation_importance
# define the model
KN = KNeighborsRegressor()
# fit the model
KN.fit(X1, target_i)
# perform permutation importance
results = permutation_importance(KN, X1, target_i, scoring='neg_mean_squared_error')
# get importance
#importance = results.importances_mean
# summarize feature importance
print( "KNeighborsRegressor features sorted by their score:")
print( sorted(zip(map(lambda x: round(x, 4), results.importances_mean), names1),reverse=True))

