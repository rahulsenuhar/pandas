import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Vikas"],
    "Age": [25, 22, 30, 27, 24],
    "City": ["Delhi", "Mumbai", "Patna", "Kolkata", "Chennai"]
}

df = pd.DataFrame(data)
print(df)
print(df.head())     # first 5 rows
print(df.tail(2))    # last 2 rows
print(df.shape)      # (rows, columns)
print(df.info())     # column names, datatypes
print(df.describe()) # stats summary (mean, std, min, max)
