import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LogisticRegression
from Logistic_Regression import load_dataset

filename = 'dataset_finale_miRNA.csv'
X, y, features = load_dataset('dataset_finale_miRNA.csv')

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)  # nomi delle classi: da string a integer

# # METODO_1
# rfe_selector = RFE(estimator=LogisticRegression(max_iter=10000), n_features_to_select=100, step=50, verbose=5)
# rfe_selector.fit(X, y)
# rfe_support = rfe_selector.get_support()
# rfe_feature = X.loc[:, rfe_support].columns.tolist()
# print(str(len(rfe_feature)), 'selected features')

# METODO_1
df = pd.DataFrame(X, columns=features)   #trasformo matrice numpy in dataframe pandas
embeded_lr_selector = SelectFromModel(LogisticRegression(penalty="l1", solver='liblinear'), max_features=200)
embeded_lr_selector.fit(X, y)

embeded_lr_support = embeded_lr_selector.get_support()
embeded_lr_feature = df.loc[:, embeded_lr_support].columns.tolist()
print(str(len(embeded_lr_feature)), 'selected features')
