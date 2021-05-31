# OLS ( ORDINARY LEAST SQUARE )

#TODO
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def msee(actual, predicted):
    sum_error = 0.0
    for i in range(len(actual)):
        prediction_error = predicted[i] - actual[i]
        sum_error += (prediction_error ** 2)
        mean_error = sum_error / float(len(actual))
    return mean_error


def Train(X, Y):
    """ With this function we are calculate the weights   """
    X.astype(float)
    first = np.dot(X.T, X)
    first.astype(np.float16)
    inverse = np.linalg.inv(first)
    second = np.dot(X.T, Y)

    b = np.dot(inverse, second)
    return b


def add_bias(x):
    if len(x.shape) == 1:
        x = x[:, np.newaxis]
    b = np.ones((x.shape[0], 1))
    x = np.concatenate((b, x), axis=1)
    return x


def predict(X, b):
    return np.dot(X, b)


df = pd.read_csv('MpgData_with_Cateogeries.csv')
col = df.columns
we = df.to_numpy()
we = we[:, 0:8]
we = we.astype(np.float64)
df.head()

xtrain = we[:292, 1:8]
ytrain = we[:292, 0]
xtest = we[292:, 1:8]
ytest = we[292:, 0]
