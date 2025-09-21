import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Vikas", "Arjun"],
    "Age": [25, 22, 30, 27, 24, 26],
    "Marks": [85, 90, 78, 92, 88, 75],
    "City": ["Delhi", "Mumbai", "Patna", "Delhi", "Mumbai", "Patna"]
}

df = pd.DataFrame(data)
print(df)

# GroupBy + Mean Average
print(df.groupby("City")["Marks"].mean())

# Multiple Aggregations

print(df.groupby("City")["Marks"].agg(["mean", "max", "min"]))

# GroupBy Multiple Columns
print(df.groupby(["City", "Age"])["Marks"].mean())

#  Multiple Columns Aggregation
print(df.groupby("City").agg({
    "Marks": "mean",
    "Age": "max"
}))
