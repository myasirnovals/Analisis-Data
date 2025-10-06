import pandas as pd

df = df.dropna()
df = df.dropna(axis=1)

df["column_name"] = df["column_name"].fillna(0)

df.fillna(method="ffill")
df.fillna(method="bfill")

df["column_name"] = df["column_name"].interpolate()