#  Write a python program to load the file student_performance_ml.csv using pandas
#  Display : 
#      First 5 records
#      Last 5 records
#      Total number of rows and columns
#      list of columns names
#      Data type of each column

# 1 : Pass
# 0 : Fail

import pandas as pd 

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

Border = "-"*40
print(Border)
print("First 5 records")
print(Border)
print(df.head())

print(Border)
print("Last 5 records")
print(Border)
print(df.tail())

print(Border)
print("Total number of rows and columns")
print(Border)
print(df.shape)

print(Border)
print("List of columns")
print(Border)
print(df.columns)

print(Border)
print("Data type of each column")
print(Border)
for i in df.columns:
    print(df[i].dtype)