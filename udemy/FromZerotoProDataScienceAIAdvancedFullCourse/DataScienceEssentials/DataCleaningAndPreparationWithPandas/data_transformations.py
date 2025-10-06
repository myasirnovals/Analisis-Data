import pandas as pd

df = df.rename(columns={"old_name": "new_name"})

df["column_name"] = df["column_name"].astype("float")
df["column_name"] = pd.to_datetime(df["column_name"])

df["column_name"] = df["existing_column"] * 2