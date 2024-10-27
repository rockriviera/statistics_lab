import numpy as np
import seaborn as sb
import pandas as pd
from scipy.stats import norm,mannwhitneyu,t
#Load data
df=pd.read_excel("Data_source.xlsx")
row_count=df.shape[0]
df=df.fillna(df.mean())
column_to_exclude='income'
df.loc[:, df.columns != column_to_exclude] = df.loc[:, df.columns != column_to_exclude].round(2)
df['income']=df['income'].round(1)

#Exercise 1.5: MWW test to see if there is diff in skill between men and women.
#Your null will be Ho : the true difference in skill is zero against H1 : true difference in mean skill is not equal to 0
women_skill=(df.loc[df['gender'] == 2])['skill'].values
men_skill=(df.loc[df['gender'] == 1])['skill'].values
n_women=women_skill.size
n_men=men_skill.size
u_women, p=mannwhitneyu(x=women_skill, y=men_skill)
# mannwhitneyu reduces the distance between the test statistic and the mean 
#by 0.5 to correct for the fact that the discrete statistic is being compared against a continuous distribution.
u_men= n_women * n_men - u_women
print(u_women, u_men, u_women+u_men, p)

#U-values show some overlap between the two groups.
#At calculated p-value 0.11, which is outside critical region 0.025 (0.11>0.025) for two-tailed test, non-rejection of H0 (skill medians are equal)

#Now we assume normality and calculate CI, two-tailed test is used to determine equality or non-equality.
#1.5:Calculating confidence interval for difference by skills between gender

#Assume unequal variances
var_men=np.var(men_skill,ddof=1)
var_women=np.var(men_skill,ddof=1)
difference_of_means=np.mean(men_skill)-np.mean(women_skill)

dof_numerator = (var_men / n_men + var_women / n_women) ** 2
dof_denominator = ((var_men / n_men) ** 2 / (n_men - 1)) + ((var_women / n_women) ** 2 / (n_women - 1))
dof = dof_numerator / dof_denominator

t_alfa0025=t.ppf(1-0.025,dof)
standard_error=np.sqrt((var_men/n_men)+(var_women/n_women))
CI_upper_bound=difference_of_means+(t_alfa0025*standard_error)
CI_lower_bound=difference_of_means-(t_alfa0025*standard_error)



print(CI_lower_bound,CI_upper_bound)

#CI includes 0 which indicates that the means are not significantly different.
# Same conclusion as mannwhitneyu, non-rejection of H0. 

