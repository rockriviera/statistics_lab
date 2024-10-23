import numpy as np
import seaborn as sb
import pandas as pd

#Load data
df=pd.read_excel("Data_source.xlsx")
row_count=df.shape[0]
df=df.fillna(df.mean())
column_to_exclude='income'
df.loc[:, df.columns != column_to_exclude] = df.loc[:, df.columns != column_to_exclude].round(2)
df['income']=df['income'].round(1)
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
#coefficients [[ 0.93783836  0.4203737   0.44643113  0.57069338  0.25436298  0.00317374
#-0.00459879]]
#intercept b0:-4.9912857
#y=-4.9912857+0.93783836x+0.4203737x²+0.44643113x³+0.57069338x⁴+0.25436298⁵+0.00317374x⁶-0.00459879x⁷
#years and age do not have significant impact on satis

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
#coefficients 0.93363321 0.42263118 0.44994538 0.57212156 0.25188117
#intercept b0: -4.98605017

#y=-4.98605017+0.93363321x+0.42263118x²+0.44994538x³+0.57212156x⁴+0.25188117x⁵