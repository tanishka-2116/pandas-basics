import pandas as pd

# create a DataFrame with numeric data
data = {
    "Marks": [85, 90, 78, 88, 92]
}

df = pd.DataFrame(data)

# basic operations
print("Marks column:")
print(df["Marks"])

print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())
