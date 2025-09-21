import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amit", "Rohit", "Neha"]
})

df2 = pd.DataFrame({
    "ID": [4, 5, 6],
    "Name": ["Priya", "Karan", "Ravi"]
})

# Row-wise 
df_row = pd.concat([df1, df2])
print(df_row)

# Column-wise 
df_col = pd.concat([df1, df2], axis=1)
print(df_col)

# merge() data

employees = pd.DataFrame({
    "EmpID": [1, 2, 3, 4],
    "Name": ["Amit", "Rohit", "Neha", "Priya"],
    "DeptID": [101, 102, 101, 103]
})

departments = pd.DataFrame({
    "DeptID": [101, 102, 103],
    "Department": ["IT", "HR", "Finance"]
})

# Inner Join (Default)
df_inner = pd.merge(employees, departments, on="DeptID", how="inner")
print(df_inner)

# Left Join
df_left = pd.merge(employees, departments, on="DeptID", how="left")
print(df_left)

# Right Join
df_right = pd.merge(employees, departments, on="DeptID", how="right")
print(df_right)

# Outer Join
df_outer = pd.merge(employees, departments, on="DeptID", how="outer")
print(df_outer)

# Index-based join
df1 = pd.DataFrame({"A": [1,2,3]}, index=["a","b","c"])
df2 = pd.DataFrame({"B": [4,5,6]}, index=["a","b","d"])

print(df1.join(df2, how="outer"))

