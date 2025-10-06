import pandas as pd
import numpy as np

df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
df2 = pd.DataFrame({"A": [1, 2, 3], "C": [4, 5, 6]})

print("Dataset 1: \n", df1, "\n")
print("Dataset 2: \n", df2, "\n")

merged = pd.merge(df1, df2, how="inner", on="A")
print("Merged dataset: \n", merged, "\n")

merged["Score_percentage"] = (merged["B"] / 100) * 100
print("Transformed dataset: \n", merged, "\n")
