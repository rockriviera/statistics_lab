# Correlation analysis, thereafter, identify the strongest correlation and statistically not significant 
#relation(s)
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("diamonds.csv")

cut_mapping = {
    'Fair': 0,
    'Good': 1,
    'Very Good': 2,
    'Premium': 3,
    'Ideal': 4
}

color_mapping = {
    'J': 0,
    'I': 1,
    'H': 2,
    'G': 3,
    'F': 4,
    'E': 5,
    'D': 6
}

clarity_mapping = {
    'I1': 0,
    'SI2': 1,
    'SI1': 2,
    'VS2': 3,
    'VS1': 4,
    'VVS2': 5,
    'VVS1': 6,
    'IF': 7
}

# Display the first few rows and the data types
print(df.head())
print(df.dtypes)

df['cut'] = df['cut'].map(cut_mapping)
df['color'] = df['color'].map(color_mapping)
df['clarity'] = df['clarity'].map(clarity_mapping)

# Display the first few rows and the data types
print(df.head())
print(df.dtypes)
correlation_matrix=df.corr(method='spearman')


plt.figure(figsize=(10, 8))
sb.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Spearman Correlation Matrix")
plt.show()