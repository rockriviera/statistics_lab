import numpy as np
import seaborn as sb
import pandas as pd
from scipy.stats import norm,kruskal, f_oneway
#Load data
df=pd.read_excel("Data_source.xlsx")
row_count=df.shape[0]
df=df.fillna(df.mean())
column_to_exclude='income'
df.loc[:, df.columns != column_to_exclude] = df.loc[:, df.columns != column_to_exclude].round(2)
df['income']=df['income'].round(1)

#Exercise 1.6: Kruskal-Wallis test to see if there is any significance in absence among ethnic group, and 
#compare with One-Way ANOVA analysis

ethnic_grp = {'White':1,'Asian':2,'West Indian':3,'African':4}
absence_whi=(df.loc[df['ethnicgp'] == 1])['absence'].values
absence_asi=(df.loc[df['ethnicgp'] == 2])['absence'].values
absence_wes=(df.loc[df['ethnicgp'] == 3])['absence'].values
absence_afr=(df.loc[df['ethnicgp'] == 4])['absence'].values

kruskal_statistic, kruskal_pvalue=kruskal(absence_whi,absence_asi,absence_wes,absence_afr)
anova_statistic, anova_pvalue=f_oneway(absence_whi,absence_asi,absence_wes,absence_afr)

print(kruskal_statistic, kruskal_pvalue)
print(anova_statistic, anova_pvalue)

#Kruskal wallis hypotheses:
    #H0: The average ranks are equal
    #H1: At least two average ranks are different
#One way ANOVA hypotheses:
    #H0: Means are equal
    #H1: At least two means are different
#One-way ANOVA compares means of at least three groups.
#Kruskal wallis test is the non-parametric version of the One-way ANOVA. 

#Both Kruskal and One-way ANOVA give a p-value around 0.3 which is higher than 95% significance (0.05).

# Non-rejection of null hypothesis, the group means are equal.