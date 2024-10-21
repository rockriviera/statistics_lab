import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
#Load data
df=pd.read_excel("Data_source.xlsx")
#note: rows containing NaN values will be dropped
#df=df.dropna()
row_count=df.shape[0]

#Exercise 1.1
#a), Pie chart ethnic group, "ethgp "Other" is not in the dataset?
ethnic_grp = {'White':1,'Asian':2,'West Indian':3,'African':4} #use in txtlabels
fractions = []
ethnic_grp_count=df['ethnicgp'].value_counts().to_dict()
df_count=df.shape[0]
offsets =(0, 0.05, 0, 0)
for grp_count in ethnic_grp_count.values():
    fractions.append(grp_count/row_count)
plt.pie(fractions, labels=list(ethnic_grp.keys()),
autopct='%1.1f%%', shadow=True, startangle=90,
colors=sb.color_palette('muted') )
plt.axis('equal')
plt.show()

#Plot of gender in bar chart
""" gender_count=df['gender'].value_counts().to_dict()
fractions=[]
for gender in gender_count.values():
    fractions.append(gender/row_count)

sb.barplot(x=["male","female"], y=fractions)
plt.show() """

#b) For column Age: 
# summarize: max, min, median, the first and third quartiles and then a box-plot
min_value = df['age'].min()
max_value = df['age'].max()
mean=df['age'].mean()
std=df['age'].std()
first_quartile=df['age'].quantile(0.25)
third_quartile=df['age'].quantile(0.75)
print("min",min_value,"max",max_value, "mean",mean,"q1",first_quartile, "q3",third_quartile) 
sb.boxplot(data=df['age'])
plt.show()
#c)Histogram, mean and std of income
""" x=df.groupby(['income']).size().reset_index(name='counts')
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.hist(x,bins=range(11,22))
income=df['income'].array
std=np.std(income)
mean=np.mean(income)
plt.figtext(0.7, 0.8, f"std = {std:.2f}", fontsize=12)
plt.figtext(0.7, 0.76, f"mean = {mean:.2f}", fontsize=12)
plt.show() """