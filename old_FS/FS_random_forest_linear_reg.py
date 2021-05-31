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
names1 = np.array(data.axes[1]) #nomi delle features (geni)
#Rimozione tutte le colonne con zero valori
# for i in names1:
#     if sum(data[i]) == 0:
#         del data[i]


#Rimozione colonne con meno di n valori
# n=1 # numero di valori
# for i in names1:
#     cont = 0
#     for n in data[i]:
#         if n != 0:
#             cont += 1
#     if cont < n:
#          del data[i]

# ## Random Forest mean decrease impurity
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

# target_b = pd.get_dummies(target) # random forest non accetta come input il target sotto forma di caratteri per questo utilizzo pdgetdummies
#
# rf = RandomForestRegressor()
# rf.fit(X1,target_i)
# # print( "Random Forest features sorted by their score:")
# # print( sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names1),reverse=True)) #stampo in ordine le features
# f = open('Result_FS.txt','w+')
# feat_rf = sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names1),reverse=True)
# f.write( "Random Forest features sorted by their score:\n")
# f.write(str(feat_rf[0:20]))
# f.close()
# ## Stability selection
#
#
#
# ## Linear regression
# from sklearn.linear_model import LinearRegression
# # define the model
# model = LinearRegression()
# # fit the model
# model.fit(X1, target_i)
# # get importance
# importance = model.coef_
# # summarize feature importance
# f = open('Result_FS.txt','a+')
# f.write("\nLinear regression features sorted by their score:\n")
# feat_lr = sorted(zip(map(lambda x: round(x, 4), importance), names1),reverse=True)
# f.write(str(feat_lr[0:20]))
# f.close()
# # print( "Linear regression features sorted by their score:")
# # print( sorted(zip(map(lambda x: round(x, 4), importance), names1),reverse=True))
# # for i,v in enumerate(importance):
# # 	print('Feature: %0d, Score: %.5f' % (i,v))
# # # plot feature importance
# # pyplot.bar([x for x in range(len(importance))], importance)
# # pyplot.show()
#
# ##Logistic Regression (not works)
# # from sklearn.linear_model import LogisticRegression
# # # define the model
# # LG = LogisticRegression()
# # # fit the model
# # LG.fit(X1, target_i)
# # # get importance
# # #importance = model.coef_[0]
# # # summarize feature importance
# # print( "Logistic regression features sorted by their score:")
# # print( sorted(zip(map(lambda x: round(x, 4), LG.coef_[0]), names1),reverse=True))
#
# ##Deision tree
# from sklearn.tree import DecisionTreeRegressor
# # define the model
# DCT = DecisionTreeRegressor()
# # fit the model
# DCT.fit(X1, target_i)
# # get importance
# #importance = DCT.feature_importances_
# # summarize feature importance
# # print( "Decision tree features sorted by their score:")
# # print( sorted(zip(map(lambda x: round(x, 4), DCT.feature_importances_), names1),reverse=True))
# f = open('Result_FS.txt','a+')
# f.write("\nDecision tree features sorted by their score:\n")
# feat_dct = sorted(zip(map(lambda x: round(x, 4), DCT.feature_importances_), names1),reverse=True)
# f.write(str(feat_dct[0:20]))
# f.close()
#
# #xgboost
# from xgboost import XGBRegressor
# # define the model
# XGB = XGBRegressor()
# # fit the model
# XGB.fit(X1, target_i)
# # get importance
# #importance = model.feature_importances_
# # summarize feature importance
# # print( "XGBoost features sorted by their score:")
# # print( sorted(zip(map(lambda x: round(x, 4), XGB.feature_importances_), names1),reverse=True))
# f = open('Result_FS.txt','a+')
# f.write("\nXGBoost features sorted by their score:\n")
# feat_xgb = sorted(zip(map(lambda x: round(x, 4), XGB.feature_importances_), names1),reverse=True)
# f.write(str(feat_xgb[0:20]))
# f.close()
#
# # KNeighborsRegressor
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.inspection import permutation_importance
# # define the model
# KN = KNeighborsRegressor()
# # fit the model
# KN.fit(X1, target_i)
# # perform permutation importance
# results = permutation_importance(KN, X1, target_i, scoring='neg_mean_squared_error')
# # get importance
# #importance = results.importances_mean
# # summarize feature importance
# # print( "KNeighborsRegressor features sorted by their score:")
# # print( sorted(zip(map(lambda x: round(x, 4), results.importances_mean), names1),reverse=True))
# f = open('Result_FS.txt','a+')
# f.write("\nKNeighborsRegressor features sorted by their score:\n")
# feat_kn= sorted(zip(map(lambda x: round(x, 4), results.importances_mean), names1),reverse=True)
# f.write(str(feat_kn[0:20]))
# f.close()

#PLS
# from sklearn.cross_decomposition import PLSRegression
# # define the model
# PLS = PLSRegression(n_components=7)
# PLS.fit(X1, target_i)

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
idx =np.where(support)[0] #indici dove support è True
f = open('Result_FS.txt','a+')
f.write("\nRFECV features:\n")
f.write(str(names1[idx]))
f.close()

