#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Ken
git : https://github.com/PlayingNumbers/ds_salary_proj
Tutorial(youtube) : https://www.youtube.com/watch?v=QWgg4w1SpJ8&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t&index=5

Inspired by (Tutorial) : https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

Disclaimer: I don't own the copyrights of the code , It was written and coded as
            followed on the youtube channel as mentioned above, I have add extra comments for 
            my reference to make code understandable.please take a note that I have changed the names of the column and files according to my need
                   , if you are copy pasting this code you have to look for syntax errors in names of files and
                   data-columns that are used in tutorial.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
df = pd.read_csv('eda_data.csv')

#A) choose relevant columns

df.columns

# df_custom_Model = df[['choose the columns you want']] <--- in this case it is already been done
df_model = df

#B) get dummy data

df_dum = pd.get_dummies(df_model)


#C) train test split

from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary', axis = 1)
y = df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=12)

#D) multiple linear regression
# import statsmodel

import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso

from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error',cv = 3))

from sklearn.metrics import SCORERS
# SCORERS.keys()
# sorted(sklearn.metrics,SCORERS.keys())
cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error')
cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error',cv = 3)
np.mean(cross_val_score(lm,X_train,y_train, scoring = 'neg_mean_absolute_error',cv = 3))

#E) lasso regression

lm_l = Lasso(alpha=.13)
lm_l.fit(X_train,y_train)
np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error',cv = 3))

alpha = []
error = []

for i in range (100):
    alpha.append(i/10)
    lml = Lasso(alpha = (i /10))
    # error.append(cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_absolute_error',cv = 3))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_absolute_error',cv = 3)))
plt.plot(alpha,error)

err= tuple(zip(alpha,error))
df_err = pd.DataFrame(err, columns = ['alpha', 'error'])
df_err[df_err.error == max(df_err.error)]

#F) random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3))

#E) tune models GridsearchCSV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,100,10),'criterion':('mse','mae'),'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error', cv = 3)
gs.fit(X_train,y_train)

gs.best_score_
gs.best_estimator_

#G) test ensembles
tpread_lm = lm.predict(X_test )
tpread_lml = lm_l.predict(X_test)
tpread_rf = gs.best_estimator_.predict(X_test)


from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, tpread_lm)
mean_absolute_error(y_test, tpread_lml)
mean_absolute_error(y_test, tpread_rf)

mean_absolute_error(y_test,(tpread_lm+tpread_rf)/2)

# now made pickle file out of this model building and used it as a form of API
# to make it work with flask server and applications

import pickle
pickl = {'model': gs.best_estimator_}
pickle.dump( pickl, open('model_file'+".p","wb"))

file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled) 
    model = data['model']

model.predict(X_test.iloc[1,:].values.reshape(1,-1))

# X_test.iloc[1,:].values.reshape(1,-1)
# list(X_test.iloc[1,:])
