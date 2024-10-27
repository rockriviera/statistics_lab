import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

#Load data
df=pd.read_csv("diamonds.csv")
#df=df.dropna()
row_count=df.shape[0]

#Carat boxplot
""" min_value = df['carat'].min()
max_value = df['carat'].max()
mean=df['carat'].mean()
std=df['carat'].std()
first_quartile=df['carat'].quantile(0.25)
third_quartile=df['carat'].quantile(0.75)
#print("min",min_value,"max",max_value, "mean",mean,"q1",first_quartile, "q3",third_quartile) 
carat_stats = df['carat'].describe()
print(carat_stats)
sb.boxplot(data=df['carat'])
plt.show() """

#Table boxplot
""" min_value = df['table'].min()
max_value = df['table'].max()
mean=df['table'].mean()
std=df['table'].std()
first_quartile=df['table'].quantile(0.25)
third_quartile=df['table'].quantile(0.75)
#print("min",min_value,"max",max_value, "mean",mean,"q1",first_quartile, "q3",third_quartile) 
table_stats = df['table'].describe()
print(table_stats)
sb.boxplot(data=df['table'])
plt.show() """

#Pie chart of Cut
""" grp = {'Fair':1,'Good':2,'Very Good':3,'Premium':4, 'Ideal':5} #use in txtlabels
fractions = []
print(df['cut'].value_counts())
grp_count=df['cut'].value_counts().reindex(grp.keys(), fill_value=0)
df_count=df.shape[0]
for count in grp_count:
    fractions.append(count/df_count)
plt.pie(fractions, labels=list(grp.keys()),
autopct='%1.1f%%', startangle=90,
colors=sb.color_palette('muted') )
plt.axis('equal')
plt.show() """

#Pie chart of Color grade
grp = {'J':1,'I':2,'H':3,'G':4, 'F':5, 'E':6, 'D':7} #use in txtlabels
fractions = []
print(df['color'].value_counts())
grp_count=df['color'].value_counts().reindex(grp.keys(), fill_value=0)
df_count=df.shape[0]
for count in grp_count:
    fractions.append(count/df_count)
plt.pie(fractions, labels=list(grp.keys()),
autopct='%1.1f%%', startangle=90,
colors=sb.color_palette('muted') )
plt.axis('equal')
plt.show()