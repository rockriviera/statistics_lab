import numpy as np
import seaborn as sb
import pandas as pd
from scipy.stats import chi2_contingency
#Load data
df=pd.read_excel("Data_source.xlsx")
row_count=df.shape[0]
df=df.fillna(df.mean())
column_to_exclude='income'
df.loc[:, df.columns != column_to_exclude] = df.loc[:, df.columns != column_to_exclude].round(2)
df['income']=df['income'].round(1)

#Re-code the variable “income” into “income_class “ with proper choice of limits of class classification 
#(suggestion: low income class [Min, Q1], middle income class (Q1, Q3], high income class (Q3, Max])
Q1=df['income'].quantile(0.25)
Q3=df['income'].quantile(0.75)
min_income=df['income'].min()
bins=[min_income,Q1,Q3,np.inf]
df['income_class'] = pd.cut(df['income'], bins, labels=['low', 'medium', 'high'])
#Investigate if there is any significant relationship between income_class and skill.
#This is done by generating a contingency table for the expected frequencies and performing a chi-square test of independence using it.
contingency_table=pd.crosstab(df['income_class'],df['skill'])
print(contingency_table)
res=chi2_contingency(contingency_table)
print(res.pvalue, res.statistic)
#H0: two variables are not associated
#H1: two variables are associated
# p-value 0.12540828571466 which is above 0.05 leads to non-rejection of H0.