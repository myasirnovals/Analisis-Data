import pandas as pd

data = {
    "Class": ["A", "A", "B", "B", "C"],
    "Score": [85, 90, 70, 65, 80],
    "Age": [24, 22, 19, 17, 21]
}

df = pd.DataFrame(data)

print("Original DataFrame: \n", df, "\n")

grouped = df.groupby("Class").mean()
print("Grouped DataFrame: \n", grouped, "\n")

stats = df.groupby("Class").agg(
    {"Score": ["mean", "max", "min"], "Age": ["mean", "max", "min"]}
)
print("Grouped DataFrame with stats: \n", stats, "\n")