import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

#Load data
df=pd.read_excel("Data_source.xlsx")
row_count=df.shape[0]
df=df.fillna(df.mean())
column_to_exclude='income'
df.loc[:, df.columns != column_to_exclude] = df.loc[:, df.columns != column_to_exclude].round(2)
df['income']=df['income'].round(1)
#Exercise 1.2
#a) Scatterplot with income as independent variable and absence.
""" sb.scatterplot(x=df['absence'],y=df['income'])
plt.show() """

#b) Simple regression model and determination coefficient, "rated" absence?
from sklearn.linear_model import LinearRegression
x=df['absence'].values.reshape(-1,1)
y=df['income'].values.reshape(-1,1)
model = LinearRegression()
model.fit(x,y)

r_sq=model.score(x,y)
print("coefficient of determination", model.score(x,y))
print("slope b1", model.coef_)
print("intercept b0", model.intercept_)
#coefficient of determination 0.06193728188201264
#slope b1 -0.14277317
#intercept b0 16.30548446
#estimated line: y=-0.14277317x+16.30548446