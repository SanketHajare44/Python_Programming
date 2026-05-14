# write a program to
#     Display total number of students in the dataset
#     Count how many students passed (FinalResult = 1)
#     Count how many students Failed (FinalResult = 0)

import pandas as pd 
Border = "-"*40

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print(Border)
print("Display total number of students in the dataset : ")

print(df.shape[0])

print(Border)
print("Count how many students passed : ")

Passed = (df["FinalResult"] == 1).sum()
print(Passed)

print(Border)
print("Count how many students Failed : ")

Failed = (df["FinalResult"] == 0).sum()
print(Failed)


