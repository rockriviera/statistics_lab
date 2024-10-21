import numpy as np
import seaborn as sb
import pandas as pd
from scipy.stats import norm
#Load data
df=pd.read_excel("Data_source.xlsx")
#note: rows containing NaN values will be dropped
df=df.dropna()
row_count=df.shape[0]
z_alfa=norm.ppf(1-0.05)
#Exercise 1.4 Find CI (alfa=0.05): 
#1.Job satisfaction.
""" satis=df['satis']
CI_offset=(z_alfa/2)*(np.std(satis)/np.sqrt(row_count))
CI_lower=np.mean(satis)-CI_offset
CI_upper=np.mean(satis)+CI_offset
print("lower",CI_lower)
print("upper",CI_upper) """
#2.Difference in satis between men and women.
men_satis=(df.loc[df['gender'] == 1])['satis'].values
women_satis=(df.loc[df['gender'] == 2])['satis'].values
CI_offset=(z_alfa/2)*np.sqrt((np.var(men_satis)/men_satis.size)+(np.var(women_satis)/women_satis.size))
mean_diff=np.mean(men_satis)-np.mean(women_satis)
CI_lower=mean_diff-CI_offset
CI_upper=mean_diff+CI_offset

print(CI_lower) #-0.42861944858937284
print(CI_upper) #0.9544815175548889

