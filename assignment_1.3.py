import numpy as np
import seaborn as sb
import pandas as pd

#Load data
df=pd.read_excel("Data_source.xlsx")
#note: rows containing NaN values will be dropped
df=df.dropna()
row_count=df.shape[0]
#Exercise 1.3
#Study the MR model with satis as dependent and commit, autonom, income, 
#skill, rated quality, age, years as independent .

#a) Which variables do NOT have significant impact on satis ?
""" from sklearn.linear_model import LinearRegression
x=df[['commit',
     'autonom',
     'income',
     'skill',
     'qual',
     'age',
     'years']].values
y=df['satis'].values.reshape(-1,1)
model = LinearRegression()
model.fit(x,y)
print("coefficients", model.coef_)
print("intercept", model.intercept_) """
#coefficients [[ 0.88659571  0.41138014  0.55357035  0.53148748  0.2926426  -0.02328439
   #0.00913497]]
#intercept b0:-5.61624205
#y=-5.61624205+0.88659571x+0.41138014x²+0.55357035x³+0.53148748x⁴+0.2926426x⁵-0.02328439x⁶+0.00913497x⁷
#years and age does not have significant impact on satis

#b)  Find a simpler MR model with satis as dependent by deleting all  
#non-impact variables. 

from sklearn.linear_model import LinearRegression
x=df[['commit',
     'autonom',
     'income',
     'skill',
     'qual']].values
y=df['satis'].values.reshape(-1,1)
model = LinearRegression()
model.fit(x,y)
print("coefficients", model.coef_)
print("intercept", model.intercept_)
#coefficients [[0.93528483 0.40168354 0.46581393 0.54447209 0.26622325]]
#intercept b0: -5.02957902

#y=-5.02957902+0.93528483x+0.40168354x²+0.46581393x³+0.54447209x⁴+0.26622325x⁵