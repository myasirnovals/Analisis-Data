# you can use this data
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

import pandas as pd

# load data from external file
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Explore structure
print("First 5 rows: \n", df.head(), "\n")
print("Last 5 rows: \n", df.tail(), "\n")
print("Info: \n", df.info(), "\n")
print("Description: \n", df.describe(), "\n")

selected_columns = df[["species", "sepal_length"]]
print("Selected columns: \n", selected_columns, "\n")

filtered_rows = df[(df["sepal_length"] > 5.0) & (df["species"] == "setosa")]
print("Filtered rows: \n", filtered_rows, "\n")

