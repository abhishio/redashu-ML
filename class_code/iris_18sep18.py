#!/usr/bin/python3
''' Supervised Machine Learning
1) Classisfication
2) Regression
'''
#import sklearn
from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# from sklearn.cross_validation import train_test_split #Depreciated Model

iris=load_iris()

# 10% for testing remaining 90% for training
train_data, test_data, train_target, test_target = train_test_split(iris.data, iris.target, test_size=0.1)

# Calling decision tree
clf = tree.DecisionTreeClassifier()

# Calling trained algo
trained = clf.fit(train_data, train_target)

# Predict
output = trained.predict(test_data)
print('Predicted Output: ', output)

# Actual output
print("Actual Output: ", test_target)

# Accuracy Score
check = accuracy_score(test_target, output)
print(check)
