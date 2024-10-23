import numpy as np
import seaborn as sb
import pandas as pd
from scipy.stats import norm,mannwhitneyu
#Load data
df=pd.read_excel("Data_source.xlsx")
row_count=df.shape[0]
df=df.fillna(df.mean())
column_to_exclude='income'
df.loc[:, df.columns != column_to_exclude] = df.loc[:, df.columns != column_to_exclude].round(2)
df['income']=df['income'].round(1)

#Exercise 1.6: Kruskal-Wallis test to see if there is any significance in absence among ethnic group, and 
#compare with One-Way ANOVA analysis
