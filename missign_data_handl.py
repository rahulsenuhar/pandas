import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Priya", "Aman", "Sneha", "Vikas"],
    "Age": [25, np.nan, 30, 27, np.nan],
    "City": ["Delhi", "Mumbai", None, "Kolkata", "Chennai"],
    "Marks": [85, 90, np.nan, 92, 88]
}

df = pd.DataFrame(data)
print(df)

# Missing Values Check
print(df.isnull())       # True/False table
print(df.isnull().sum()) # every column how much missing values

# Drop Missing Values
print(df.dropna())

# Fill Missing Values
print(df.fillna(0))   

# Column-wise fill

print(df["Age"].fillna(df["Age"].mean()))   
print(df["Marks"].fillna(df["Marks"].median())) 
print(df["City"].fillna("Unknown"))         

# Forward Fill / Backward Fill

print(df.fillna(method="ffill"))  
print(df.fillna(method="bfill"))  

# Permanent Changes

df["Age"].fillna(df["Age"].mean(), inplace=True)
df["City"].fillna("Unknown", inplace=True)
print(df)
