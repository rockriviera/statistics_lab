#Exercise 2.6
#Study the MR model with price as dependent and commit, autonom, income, 
#skill, rated quality, age, years as independent .

#a) Which variables do NOT have significant impact on satis ?
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

import statsmodels.api as sm
df=pd.read_csv("diamonds.csv")

clarity_mapping = {
    'I1': 0,
    'SI2': 1,
    'SI1': 2,
    'VS2': 3,
    'VS1': 4,
    'VVS2': 5,
    'VVS1': 6,
    'IF': 7
}
df['clarity'] = df['clarity'].map(clarity_mapping)
x=df[['clarity',
     'x',
     'y',
     'z']].values
y=df['price'].values.reshape(-1,1)
x=sm.add_constant(x)
model = sm.OLS(y,x)
results=model.fit()
print(results.summary())
#coefficients [[ 0.93783836  0.4203737   0.44643113  0.57069338  0.25436298  0.00317374
#-0.00459879]]
#intercept b0:-4.9912857
#y=-4.9912857+0.93783836x+0.4203737x²+0.44643113x³+0.57069338x⁴+0.25436298⁵+0.00317374x⁶-0.00459879x⁷
#A p-value below 0.05 for 95% significance suggests that the coefficients have a significant effect on the dependent variable. 
#Going by p-values in the table, we can see that qual, age and years seem insignificant
#The low coefficient values for years and age are an additional indicator that those factors seem insignificant.

#b)Find a simpler MR model with satis as dependent by deleting all  
#non-impact variables. 

""" import statsmodels.api as sm
x=df[['commit',
     'autonom',
     'income',
     'skill',]].values
y=df['satis'].values.reshape(-1,1)
x=sm.add_constant(x)
model = sm.OLS(y,x)
results=model.fit()
print(results.summary()) """
#print("coefficients", model.coef_)
#print("intercept", model.intercept_)
#intercept b0: -4.2579

#y=-4.2579+0.9527x+0.4491x²+0.4385x³+0.5541x⁴
