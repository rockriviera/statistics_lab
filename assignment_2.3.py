import numpy as np
import seaborn as sb
import pandas as pd
from scipy.stats import kruskal, f_oneway
df=pd.read_csv("diamonds.csv")

#Exercise 1.6: Kruskal-Wallis test to see if there is any significance in table with among different cuts, and 
#compare with One-Way ANOVA analysis
cuts=['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
table_fair=(df.loc[df['cut'] == 'Fair'])['table'].values
table_good=(df.loc[df['cut'] == 'Good'])['table'].values
table_verygood=(df.loc[df['cut'] == 'Very Good'])['table'].values
table_premium=(df.loc[df['cut'] == 'Premium'])['table'].values
table_ideal=(df.loc[df['cut'] == 'Ideal'])['table'].values
kruskal_statistic, kruskal_pvalue=kruskal(table_fair,table_good,table_verygood,table_premium, table_ideal)
anova_statistic, anova_pvalue=f_oneway(table_fair,table_good,table_verygood,table_premium, table_ideal)

print(kruskal_statistic, kruskal_pvalue)
print(anova_statistic, anova_pvalue)