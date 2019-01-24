#!/usr/bin/python3
''' Supervised Machine Learning
1) Classisfication
2) Regression
'''

#import sklearn
from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

# random gate generator
sample = [0, 50, 150]
# Load the Iris Data
iris = load_iris()

# features are 
x = iris.data
# Lable which means output
y = iris.target

# Only picking 49 sample for data training rest one for prediction
training_data = np.delete(x, sample)

test_data = iris.data[sample]

# Lets work for label
train_target = np.delete[iris.target, sample]

# Calling decision tree
algo = tree.DecisionTreeClassifier()
#trained = algo.fit(features, ouput)
trained = algo.fit(x, y)

# Now time for arranging 
out = trained.predict(test_data)

print(out)