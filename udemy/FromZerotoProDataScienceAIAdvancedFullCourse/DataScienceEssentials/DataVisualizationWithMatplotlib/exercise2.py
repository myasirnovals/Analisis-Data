# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

del df['species']

# calculate correlation matrix
correlation_matrix = df.corr()

# plot heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()