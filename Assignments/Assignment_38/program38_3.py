# Using pandas functions, calculate and display:
#     Average StudyHours
#     Average Attendence
#     Maximum PreviousScore
#     Minimum SpleepHours

import pandas as pd 

DatasetPath = "student_performance_ml.csv"


Border = "-"*40

df = pd.read_csv(DatasetPath)

print(Border)
print("Average StudyHours")
print(df["StudyHours"].mean())

print(Border)
print("Average Attendence")
print(df["Attendance"].mean())

print(Border)
print("Maximum PreviousScore")
print(df["PreviousScore"].max())

print(Border)
print("Minimum sleephours")
print(df["SleepHours"].min())

print(df.describe())