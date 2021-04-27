from pandas import read_csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder


def load_dataset(filename):
    target = []
    # load the dataset as a pandas DataFrame
    data = read_csv(filename, index_col=[0])
    # retrieve numpy array
    X1 = data.values
    y1 = list(data.axes[0])
    for line in y1:
        line = line.strip('"(').strip("',)")
        target.append(line)  # pulisco nomi delle classi
    y1 = target
    genes = np.array(data.axes[1])  # nomi features
    return X1, y1, genes


filename = 'dataset_finale_miRNA.csv'
X, y, features = load_dataset('dataset_finale_miRNA.csv')

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)  # nomi delle classi: da string a integer

# define the model
model = LogisticRegression(max_iter=1000, solver='sag')
# fit the model
model.fit(X, y)
# get importance
importance = model.coef_[0]
for i, v in enumerate(importance):
    print('Feature: %0d, Score: %.5f' % (i, v))

# summarize feature importance
# print("Logistic regression features sorted by their score:")
# print(sorted(zip(map(lambda x: round(x, 4), importance), features), reverse=True))

# fare print su file di log ' filename+log.txt '