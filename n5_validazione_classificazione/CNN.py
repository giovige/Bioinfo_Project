from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import matplotlib as mpl
import tensorflow as tf
import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# Confusion matrix
SIZE = 13
mpl.rcParams['font.size'] = SIZE
mpl.rcParams['text.color'] = "black"
mpl.rcParams['axes.labelcolor'] = "black"
mpl.rcParams['xtick.color'] = "black"
mpl.rcParams['ytick.color'] = "black"
mpl.rcParams['xtick.labelsize'] = SIZE
mpl.rcParams['ytick.labelsize'] = SIZE
mpl.rcParams['axes.titlesize'] = SIZE
mpl.rcParams['axes.labelsize'] = SIZE
mpl.rcParams['grid.linestyle'] = "--"
mpl.rcParams['grid.linewidth'] = 0.8
mpl.rcParams['grid.color'] = [0.2, 0.2, 0.2]
mpl.rcParams['grid.alpha'] = 0.3
mpl.rcParams['axes.grid'] = True

##----------------------------------------------Plot function
class MyPlot():
    def __init__(self,
                 nrows,
                 ncols,
                 figsize):
        self.fig, self.axes = plt.subplots(nrows=nrows,
                                           ncols=ncols,
                                           figsize=figsize)

def compute_confusion_matrix(y_true, y_false):
    cm = confusion_matrix(y_true, y_false)
    return cm


def plot_confusion_matrix(cm,
                          classes,
                          normalize=True,
                          figsize=(7, 7),
                          title='Confusion matrix',
                          cmap=plt.cm.Greys):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    else:
        print('Confusion matrix without normalization')
    plt.figure(figsize=figsize)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.grid(False)



##---------------------------------------------Import Data
data_name = '' #insert data name
data = pd.read_csv(data_name, index_col=[0])
dataset = data.values
target = data.index
label_encoder = LabelEncoder()
y= label_encoder.fit_transform(target)
X_train, X_test, y_train, y_test = train_test_split(dataset, y, test_size = 0.2, random_state = 0)
class_names = ['CPTAC-3','TARGET-RT', 'TARGET-WT', 'TCGA-KICH', 'TCGA-KIRC', 'TCGA-KIRP', 'TCGA-SARC']
#c_names =  target.value_counts().index

##----------------------------------------Define model

model = tf.keras.models.Sequential([
            tf.keras.layers.Input(shape=X_train.shape[1]), #input the shape
            tf.keras.layers.Flatten(), #connection between the input layer and second layer
            tf.keras.layers.Dense(512, activation='relu', name="fc1"), #multilayer perceptron 512 neuron
            tf.keras.layers.Dropout(0.2), #dropout layer
            tf.keras.layers.Dense(len(np.unique(y_test)), activation='softmax', name="predictions") #classification layer(number of label to classify)
            ])
learning_rate = 0.1
optimizer = tf.keras.optimizers.Adam(lr=learning_rate) #Adam optimizer selected(minimization error)
model.compile(optimizer=optimizer,
                           loss='sparse_categorical_crossentropy', #loss function
                           metrics=['accuracy']) #metrics to monitor the train


#------------------------------------Classification
model.fit(X_train, y_train, validation_data=(X_test,y_test),epochs=20, batch_size=64,verbose=1)
# score = model.evaluate(X_test, y_test, batch_size=128)
# print(score)
loss, acc = model.evaluate(X_test, y_test, verbose=False);

#Predictions
predictions = model.predict(X_test)
#Plot confusion matrix
cm = compute_confusion_matrix(y_test, np.argmax(predictions, axis=1))
plot_confusion_matrix(cm, class_names, normalize=True)