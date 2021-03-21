# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:11:52 2021

@author: cacif
"""

import pandas as pd

#read a data
mat = pd.read_csv('student-mat.csv')

#check if its has any NaN value
print(mat.isna().sum())

# GP = 0, MS = 1
mat['school'] = mat['school'].map({'GP': 0, 'MS': 1}).astype(int)

# M = 0, F = 1
mat['sex'] = mat['sex'].map({'M': 0, 'F': 1}).astype(int)

# Rural(R) = 0, Urban(U) =  1
mat['address'] = mat['address'].map({'R': 0, 'U': 1}).astype(int)

# Less then 3(LE3) = 0, Greater then 3(GT3) = 1
mat['famsize'] = mat['famsize'].map({'LE3': 0, 'GT3': 1}).astype(int)

# Living together(T) = 1, Apart(A) = 0
mat['Pstatus'] = mat['Pstatus'].map({'A': 0, 'T': 1}).astype(int)

# Male jobs: at_home = 0, health = 1, other = 2, services = 3, teacher = 4
mat['Mjob'] = mat['Mjob'].map({'at_home': 0, 'health': 1, 'other': 2, 'services': 3, 'teacher': 4}).astype(int)

# female jobs: at_home = 0, health = 1, other = 2, services = 3, teacher = 4
mat['Fjob'] = mat['Fjob'].map({'at_home': 0, 'health': 1, 'other': 2, 'services': 3, 'teacher': 4}).astype(int)

# reason to choose this school: course = 0, other = 1, home = 2, reputation = 3
mat['reason'] = mat['reason'].map({'course': 0, 'other': 1, 'home': 2, 'reputation': 3}).astype(int)

# guardian: mother = 0, father = 1, other = 3 
mat['guardian'] = mat['guardian'].map({'mother': 0, 'father': 1, 'other': 2}).astype(int)

# extra educational support: no = 0, yes = 1
mat['schoolsup'] = mat['schoolsup'].map({'no': 0, 'yes': 1}).astype(int)

# family educational support: no = 0, yes = 1
mat['famsup'] = mat['famsup'].map({'no': 0, 'yes': 1}).astype(int)

# extra paid classes: no = 0, yes = 1
mat['paid'] = mat['paid'].map({'no': 0, 'yes': 1}).astype(int)

# extra-curricular activities: no = 0, yes = 1
mat['activities'] = mat['activities'].map({'no': 0, 'yes': 1}).astype(int)

# attended nursery school: no = 0, yes = 1
mat['nursery'] = mat['nursery'].map({'no': 0, 'yes': 1}).astype(int)

# wants to take higher education: no = 0, yes = 1 
mat['higher'] = mat['higher'].map({'no': 0, 'yes': 1}).astype(int)

# Internet access at home: no = 0, yes = 1
mat['internet'] = mat['internet'].map({'no': 0, 'yes': 1}).astype(int)

# with a romantic relationship: no = 0, yes = 1
mat['romantic'] = mat['romantic'].map({'no': 0, 'yes': 1}).astype(int)

mat.to_csv('mat_grades_data_cleaned.csv', index = False)
