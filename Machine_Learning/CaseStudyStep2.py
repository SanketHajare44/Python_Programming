import pandas as pd 

import matplotlib.pyplot as plt 

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier,plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

Border = "-"*40

#################################################################
# Step 1 : Load the Dataset
#################################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DatasetPath = "iris.csv"

# df -> DataFrame
df = pd.read_csv(DatasetPath)

print("Dataset gets loaded succesfully...")
print("Initial entry from dataset : ")
print(df.head())

#################################################################
# Step 2 : Data Analysis (EDA)
#################################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of Dataset : ",df.shape)  # it gives the row*column

print("Column Names : ",list(df.columns))

print("Missing values (per column)")
print(df.isnull().sum())

print("Class Distribution (species count)")
print(df["species"].value_counts())

print("Statistical report  of Dataset")
print(df.describe())

'''
Output : 

sanket-hajare@sanket:~/PPA2/Python_Programming/Machine_Learning$ python3 CaseStudyStep3.py
----------------------------------------
Step 1 : Load the Dataset
----------------------------------------
Dataset gets loaded succesfully...
Initial entry from dataset : 
   sepal length (cm)  sepal width (cm)  ...  petal width (cm)  species
0                5.1               3.5  ...               0.2   Setosa
1                4.9               3.0  ...               0.2   Setosa
2                4.7               3.2  ...               0.2   Setosa
3                4.6               3.1  ...               0.2   Setosa
4                5.0               3.6  ...               0.2   Setosa

[5 rows x 5 columns]
----------------------------------------
Step 2 : Data Analysis
----------------------------------------
Shape of Dataset :  (150, 5)
Column Names :  ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'species']
Missing values (per column)
sepal length (cm)    0
sepal width (cm)     0
petal length (cm)    0
petal width (cm)     0
species              0
dtype: int64
Class Distribution (species count)
species
Setosa        50
Versicolor    50
Virginica     50
Name: count, dtype: int64
Statistical report  of Dataset
       sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
count         150.000000        150.000000         150.000000        150.000000
mean            5.843333          3.057333           3.758000          1.199333
std             0.828066          0.435866           1.765298          0.762238
min             4.300000          2.000000           1.000000          0.100000
25%             5.100000          2.800000           1.600000          0.300000
50%             5.800000          3.000000           4.350000          1.300000
75%             6.400000          3.300000           5.100000          1.800000
max             7.900000          4.400000           6.900000          2.500000
sanket-hajare@sanket:~/PPA2/Python_Programming/Machine_Learning$ 

'''



