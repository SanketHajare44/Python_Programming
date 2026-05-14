# Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of pass and fail students
# Is the Dataset balanced? Justify your answer

import pandas as pd

DatasetPath = "student_performance_ml.csv"

Border = "-"*40

df = pd.read_csv(DatasetPath)

print(Border)
print("Percentage of Pass : ",((df["FinalResult"] == 1).sum() / df.shape[0])*100)

print("Percentage of Fail : ",((df["FinalResult"] == 0).sum() / df.shape[0])*100)

'''
Is the data set is balanced? :
-> 50% - 50% is perfectly balanced
   60% - 40% also balanced
    but 70% - 30% is  imbalanced 

'''