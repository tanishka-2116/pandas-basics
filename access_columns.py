import pandas as pd

# create a DataFrame
data = {
    "Name": ["Amit", "Neha", "Ravi"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

# access single column
print("Names column:")
print(df["Name"])

print("\nMarks column:")
print(df["Marks"])
