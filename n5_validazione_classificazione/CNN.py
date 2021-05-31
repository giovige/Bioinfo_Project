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

def my_histogram(ax, data, color, title=None, rwidth=None, log=True, bins=25, align='mid', density=None):
    ax.hist(data, color=color, log=log, bins=bins, edgecolor='black', linewidth=1.2, rwidth=rwidth, align=align,
            density=density);
    ax.set_title(title);

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
mi_data = pd.read_csv('CCA_result_dataset.csv', index_col=[0])
dataset = mi_data.values
target = mi_data.index
label_encoder = LabelEncoder()
y= label_encoder.fit_transform(target)
X_train, X_test, y_train, y_test = train_test_split(dataset, y, test_size = 0.4, random_state = 0)
class_names = ['CPTAC-3','TARGET-RT', 'TARGET-WT', 'TGCA-KICH', 'TGCA-KIRC', 'TGCA-KIRP', 'TGCA-SARC']
class_names_3_label = ['CPTAC-3','TARGET', 'TGCA']
##----------------------------------------Define model

model = tf.keras.models.Sequential([
            tf.keras.layers.Input(shape=X_train.shape[1]),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(512, activation='relu', name="fc1"),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(len(np.unique(y_test)), activation='softmax', name="predictions")
            ])
learning_rate = 0.1
optimizer = tf.keras.optimizers.Adam(lr=learning_rate)
model.compile(optimizer=optimizer,
                           loss='sparse_categorical_crossentropy',
                           metrics=['accuracy'])

model.fit(X_train, y_train, validation_data=(X_test,y_test),epochs=20, batch_size=64,verbose=1)
# score = model.evaluate(X_test, y_test, batch_size=128)
# print(score)
loss, acc = model.evaluate(X_test, y_test, verbose=False);

#CM
predictions = model.predict(X_test)
cm = compute_confusion_matrix(y_test, np.argmax(predictions, axis=1))
plot_confusion_matrix(cm, class_names, normalize=True)