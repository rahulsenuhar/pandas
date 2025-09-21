import pandas as pd

 # Creating  Series data

data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)

# customized series 
data = pd.Series([11,12,13,14], index=['a','b','c','d'])
print(data)

# without indexing
# dataa = pd.Series([1,2,3], index = False)
#print("data without indexing",dataa )

# 2d Datafram 
data = {
    "Name":["Rahul","Radha","Krishna"],
    "Age":[20,21,22],
    "city":["siwan","varsana","gokul"]
}
df = pd.DataFrame(data)
print(df)