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

#Exercise 1.5: MWW test to see if there is diff in skill between men and women.
women_skill=(df.loc[df['gender'] == 2])['skill'].values
men_skill=(df.loc[df['gender'] == 1])['skill'].values
women_count=women_skill.size
men_count=men_skill.size
u_women, p=mannwhitneyu(x=women_skill, y=men_skill)
# mannwhitneyu reduces the distance between the test statistic and the mean 
#by 0.5 to correct for the fact that the discrete statistic is being compared against a continuous distribution.
u_men= women_count * men_count - u_women
print(u_women, u_men, u_women+u_men, p)

#U-values show some overlap between the two groups.
#At calculated p-value 0.11, which is outside critical region 0.05 (0.11>0.05) for one-tailed test, do not reject H0 (skill means are equal)
