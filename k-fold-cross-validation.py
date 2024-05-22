# perform k-fold cross validation

import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

# load the dataset
filename = "pima-indians-diabetes.data.csv"
names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
dataframe = pd.read_csv(filename, names=names)
array = dataframe.values
X = array[:, 0:8]
Y = array[:, 8]

# prepare the cross-validation procedure
kfold = KFold(n_splits=10, random_state=7)
model = LogisticRegression(max_iter=1000)
results = cross_val_score(model, X, Y, cv=kfold)

# print the results
print("Accuracy: %.3f%% (%.3f%%)" % (results.mean() * 100.0, results.std() * 100.0))
