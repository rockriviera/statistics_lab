import numpy as np
import seaborn as sb
import pandas as pd
from scipy.stats import norm
#Load data
df=pd.read_excel("Data_source.xlsx")
#note: rows containing NaN values will be dropped
df=df.dropna()
row_count=df.shape[0]

#Exercise 1.5: MWW test to see diff