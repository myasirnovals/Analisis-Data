import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)

data = {
    "Name": ["Alice", "Bob"],
    "Age": [20, 30],
    "City": ["New York", "Paris"],
    "Country": ["USA", "France"],
    "Birthdate": ["2000-01-01", "1990-02-02"],
    "Birthplace": ["New York", "Paris"],
    "Birthplace_City": ["New York City", "Paris"],
    "Birthplace_Country": ["USA", "France"],
    "Birthplace_Year": ["2000", "1990"],
    "Birthplace_Month": ["January", "February"],
    "Birthplace_Day": ["01", "02"],
}

df = pd.DataFrame(data)
print(df)

# load data from external file
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# saving data to external file
df.to_csv("data_output.csv", index=False)
df.to_excel("data_output.xlsx", index=False)

# view data info
print(df.head())
print(df.info())
print(df.tail(3))
print(df.describe())

# view data specific column
print(df["Name"])
print(df[["Name", "Age"]])
print(df.loc[0, "Name"])
print(df.iloc[0, 0])
