# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:42:17 2021

@author: cacif
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data_eda.csv')

print(df.corr()['total_grades'].sort_values(ascending=False))

grades_corr = df.corr()['total_grades']

grades_corr = pd.DataFrame({'col':grades_corr.index, 'correlation':grades_corr.values})

no_corr_cols = grades_corr[(grades_corr.correlation < 0.1) & (grades_corr.correlation > -0.1)]
no_corr_cols = list(no_corr_cols.col)

X = df.drop(['G1', 'G2', 'G3', 'total_grades'], axis=1)
y = df['total_grades']

X = X.drop(no_corr_cols, axis=1)

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score

models = [LinearRegression(), Ridge(), Lasso(), DecisionTreeRegressor()]
names = ['LinearRegression', 'Ridge', 'Lasso', 'DecisionTreeRegressor']

for name, clf in zip(names, models):
    cv_model = cross_val_score(clf, X, y, cv=5).mean()
    print(name, ': %s' % cv_model)
    

dtr = DecisionTreeRegressor()
cvs = range(2,20)
cvs_models = []
for i in cvs:
    cvs_models.append(abs(cross_val_score(clf, X, y, cv=i).mean()))
    
print('Best score with', cvs_models.index(min(cvs_models)), 'subsets : %s' % max(cvs_models))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

dtr = DecisionTreeRegressor()

dtr.fit(X_train, y_train)

score = dtr.score(X_test,y_test)

print(score)