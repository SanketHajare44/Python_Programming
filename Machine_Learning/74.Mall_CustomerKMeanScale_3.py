import pandas as pd 
import matplotlib.pyplot as plt 

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():

    #===============================================================
    #   Step 1 : Load the dataset
    #===============================================================

    print("Step 1 : Load the dataset")
    df = pd.read_csv("Mall_Customers.csv")

    print("\nFirst few records : ")
    print(df.head())

    print("\nShape of dataset : ")
    print(df.shape)

    print("\nMissing values : ")
    print(df.isnull().sum())


    #===============================================================
    #   Step 2 : Select Features (Independent)
    #===============================================================

    print("\nStep 2 : Select Features (Independent)")

    X = df[["AnnualIncome", "SpendingScore"]]

    print("\nSelected features : ")
    print(X.head())

    print("\nShape of selected features : ")
    print(X.shape)

    #===============================================================
    #   Step 3 : Scale the data
    #===============================================================

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)

    print("\nData After scalling : ")
    print(X_scaled[:5])

if __name__=="__main__":
    main()