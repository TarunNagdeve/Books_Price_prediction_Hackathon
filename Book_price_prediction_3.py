import pandas as pd
import numpy as np
import re
from xgboost import XGBRegressor
import math
import seaborn as sns
import matplotlib.pyplot as plt
train=pd.read_csv(r'C:\Users\TARUN\Desktop\New folder (3)\Book_price_prediction\Participants_Data\Train1.csv')
#np.sqrt(np.square(np.log10(y_pred +1) - np.log10(y_true +1)).mean())
train['new_1']=train['Reviews']//train['Ratings']




Labels=train['Price']
train=train.drop('Unnamed: 0',axis=1)
train=train.drop('Price',axis=1)
Features=train[:]
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_sc=sc.fit_transform(Features)

from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor


xtrain, xtest, ytrain, ytest = train_test_split(x_sc, Labels, test_size=0.3, random_state=84)
xmodel = XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
                          colsample_bynode=1, colsample_bytree=0.3, gamma=0,
                          importance_type='gain', learning_rate=0.1, max_delta_step=0,
                          max_depth=8, min_child_weight=1, missing=None, n_estimators=100,
                          n_jobs=1, nthread=None, objective='reg:linear', random_state=0,
                          reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
                          silent=None, subsample=1, verbosity=1)


# xmodel.fit(x_sc,Labels)
cmodel = cross_validate(estimator=xmodel, X=x_sc, y=Labels)

print(np.mean(cmodel['test_score']))

test=pd.read_csv(r'C:\Users\TARUN\Desktop\New folder (3)\Book_price_prediction\Participants_Data\Test.csv')
test=test.drop('Unnamed: 0',axis=1)
test_features=test[:]
test_sc=sc.transform(test_features)
ans=xmodel.predict(test_sc)
df=pd.DataFrame(ans)
df.to_csv(r'C:\Users\TARUN\Desktop\New folder (3)\Book_price_prediction\Participants_Data\S3.csv')

