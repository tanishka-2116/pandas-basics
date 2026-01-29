import pandas as pd

# creating a DataFrame
data = {
    "Name": ["Amit", "Neha", "Ravi"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# check column names
print("Columns:", df.columns)

# check shape (rows, columns)
print("Shape:", df.shape)

# detailed information
print("\nDataFrame Info:")
print(df.info())
