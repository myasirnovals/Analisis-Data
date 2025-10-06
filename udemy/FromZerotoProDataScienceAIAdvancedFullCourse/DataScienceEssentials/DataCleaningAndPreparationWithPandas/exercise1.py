import pandas as pd
import numpy as np

# create a sample dataset
data = {
    "Name": ["Alice", "Bob", np.nan, "David", "Eve", np.nan],
    "Age": [25, 30, 27, 35, 28, np.nan],
    "Score": [65, np.nan, 50, np.nan, 70, np.nan],
}

df = pd.DataFrame(data)

print("Original data frame: \n", df, "\n")

# cleaning data
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()

print("Cleaned data frame: \n", df, "\n")

# rename column
df = df.rename(columns={"Name": "Student_Name", "Score": "Exam_Score"})
print("Renamed data frame: \n", df, "\n")
