import numpy as np
import seaborn as sb
import pandas as pd
from scipy.stats import norm,t
df=pd.read_csv("diamonds.csv")
row_count=df.shape[0]
dof=row_count-1
z_alfa=norm.ppf(1-0.025)
#Exercise 2.2 Find CI for(alfa=0.05): 
#1.Carat (Population mean μ (sample std (s) converging to σ so it will be used.)).
""" carat=df['carat']
CI_offset=(z_alfa)*(np.std(carat)/np.sqrt(row_count))
CI_lower=np.mean(carat)-CI_offset
CI_upper=np.mean(carat)+CI_offset
print("lower",CI_lower)
print("upper",CI_upper) """
#lower 10.081149083342035
#upper 11.595422345229396
#Confidence interval is narrow, does this mean something?
#2.Difference in price between 'Fair' and 'Good' cuts.
print(df['price'].describe())
fair_cut=(df.loc[df['cut'] == 'Fair'])['price'].values
good_cut=(df.loc[df['cut'] == 'Good'])['price'].values
CI_offset=(z_alfa)*np.sqrt((np.var(fair_cut)/fair_cut.size)+(np.var(good_cut)/good_cut.size))
mean_diff=np.mean(fair_cut)-np.mean(good_cut)
CI_lower=mean_diff-CI_offset
CI_upper=mean_diff+CI_offset

print(CI_lower) 
print(CI_upper) 
#lower -1.2967916989868515
#upper 1.7584625013028161
#CI includes 0 which indicates that the means are not significantly different.
