# -*- coding: utf-8 -*-
"""kaggle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wLR3EGV30o4HYiskVgCEZN9C1F48Lq12
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.externals import joblib
# %matplotlib inline

df = pd.read_csv('/content/drive/MyDrive/Diabetes Prediction/diabetes.csv')
df.head()

df.info()

df.groupby('Outcome').agg('count')

df.describe()

df.hist(bins = 50,figsize=(20,15))

corr_matrix = df.corr()
corr_matrix['Outcome'].sort_values(ascending = False)

x = df.drop(['Outcome'],axis = 'columns')
y = df[['Outcome']]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3)

model = LinearRegression()
model.fit(x_train,y_train)
model.score(x_test,y_test)

model = LogisticRegression()
model.fit(x_train,y_train)
model.score(x_test,y_test)

model = SVC()
model.fit(x_train,y_train)
model.score(x_test,y_test)

model = DecisionTreeClassifier()
model.fit(x_train,y_train)
model.score(x_test,y_test)

model = Lasso()
model.fit(x_train,y_train)
model.score(x_test,y_test)

model = Ridge(alpha = 0.1)
model.fit(x_train,y_train)
model.score(x_test,y_test)

model = LogisticRegression()
model.fit(x_train,y_train)
model.score(x_test,y_test)

joblib.dump(model, 'model.pkl')

array =np.array([8,183,64,0,0,23.3,0.672,32])
model.predict([array])[0]