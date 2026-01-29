import pandas as pd

# creating a simple table
data = {
    "Name": ["Era", "Neha", "Ranu"],
    "Age": [20, 21, 19]
}

df = pd.DataFrame(data)

print(df)
