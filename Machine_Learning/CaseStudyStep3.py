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

print("Shape of Dataset : ",df.shape)  # it gives the row*column  (if row contains multiple  and row contains 1 then in result of shape second parameter is missing )

print("Column Names : ",list(df.columns))

print("Missing values (per column)")
print(df.isnull().sum())

print("Class Distribution (species count)")
print(df["species"].value_counts())

print("Statistical report  of Dataset")
print(df.describe())

#################################################################
# Step 3 : Decide Independent(Features) and Dependent(Labels) variables
#################################################################

print(Border)
print("Step 3 : Decide Independent and Dependent variables")
print(Border)

# X : Independent variables / Features 
# Y : dependent variables / Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
]

X = df[feature_cols]
Y = df["species"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)


