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
import seaborn as sns
from sklearn.cluster import KMeans

# %matplotlib inline

df = pd.read_csv('/content/drive/MyDrive/parkinsons_disease_predictor/parkinsons.data')
df

df.info()

df = df.drop(columns = ['name'])

df.head()

df.describe()

df.status.unique()

corr_matrix = df.corr()
corr_matrix['status'].sort_values(ascending = False)

df1 = df[['spread1', 'PPE','spread2','MDVP:Fo(Hz)','status']]
sns.pairplot(df1)

x = df.drop(columns=['status'])
y = df['status']

"""Splitting attributes into training and testing dataset"""

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.3)

len(x_test)

"""Function to check best model for training the dataset"""

def check(model):
  score = 0
  for model in model:
    model.fit(x_train,y_train)
    model_name = type(model).__name__
    temp_score = model.score(x_test,y_test)
    if temp_score>score:
      score = temp_score
      model_name_best = model_name
      model_final = model
    print(model_name,temp_score)
    print('\n')
  print('The best model is : ',model_name_best,score)
  print('\n')
  return model_final

"""Input model Array and Getting result"""

model = [LinearRegression(),LogisticRegression(), SVC(), DecisionTreeClassifier(), Lasso(),Ridge()]
model = check(model)

"""Tesing the predicted value of model with Actual value"""

df.result = df.status
arr = [198.764,396.961,74.904,0.00740,0.00004,0.00370,0.00390,0.01109,0.02296,0.241,0.01265,0.01321,0.01588,0.03794,0.07223,19.020,0.451221,0.643956,-6.744577,0.207454,2.138608,0.123306]

input = np.array(arr)
predicted = model.predict([input])[0]
Actual = df.result.iloc[193]
print('The Predicted value is: ', predicted)
print('The Actual value is: ', Actual)

cd /content/drive/MyDrive/parkinsons_disease_predictor

joblib.dump(model, 'model.pkl')