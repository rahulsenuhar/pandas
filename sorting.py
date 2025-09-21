import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Vikas"],
    "Age": [25, 22, 30, 27, 24],
    "Marks": [85, 90, 78, 92, 88],
    "City": ["Delhi", "Mumbai", "Patna", "Kolkata", "Chennai"]
}

df = pd.DataFrame(data)
print(df)

# Sorting by Single Column

#  ascending sort
print(df.sort_values("Age"))

# descending sort
print(df.sort_values("Marks", ascending=False))

# Sorting by Multiple Columns
#  City alphabetically, Marks descending

print(df.sort_values(by=["City", "Marks"], ascending=[True, False]))

# Sorting by Index
print(df.sort_index())        # index ascending
print(df.sort_index(ascending=False))  # index descending


