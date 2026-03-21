import pandas as pd 
import numpy as np 
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

#----------------------------------------------------------------
#   Function name : ShowData
#   Description :   It shows basic information about dataset
#   Parameters :    df
#                   df -> Pandas dataframe object
#                   messsge
#                   messsge -> Heading text to display
#   Return :        None
#   Date :          14/03/2026
#   Author :        Sanket Sadashiv Hajare
#----------------------------------------------------------------

def ShowData(df,messsge):
    DisplayInfo(messsge)
    
    print("\nFirst five rows of dataset : ")
    print(df.head())

    print("\nShape of dataset : ")
    print(df.shape)

    print("\nColumn names : ")
    print(df.columns.tolist())

    print("\nMissing values in each column : ")
    print(df.isnull().sum())


#----------------------------------------------------------------
#   Function name : DisplayInfo
#   Description :   It dsiplays the formated title
#   Parameters :    title (Str)
#   Return :        None
#   Date :          14/03/2026
#   Author :        Sanket Sadashiv Hajare
#----------------------------------------------------------------

def DisplayInfo(title):
    print("\n"+"="*70)
    print(title)
    print("="*70)

#----------------------------------------------------------------
#   Function name : CleanTitanicData
#   Description :   It does pre-processing
#                   It removes unnecessary columns
#                   It handels missing values
#                   It converts text data into numeric format
#                   It does encoding to catogiricalm columns
#   Parameters :    df -> pandas dataframe
#   Return :        df -> Clean pandas dataframe
#   Date :          14/03/2026
#   Author :        Sanket Sadashiv Hajare
#----------------------------------------------------------------

def CleanTitanicData(df):
    DisplayInfo("Step 2 : Original data")
    print(df.head())

    # Remove unnecessary columns
    drop_columns = ["Passengerid","zero","Name","Cabin"]
    existing_coulumns = [col for col in drop_columns if col in df.columns]

    print("\nColumns to be dropped")
    print(existing_coulumns)

    # drop the unwanted columns
    df = df.drop(columns = existing_coulumns)

    DisplayInfo("Step 2 : Data after column removal")
    print(df.head())

    # Handel age column
    if "Age" in df.columns:
        print("Age column before filling missing values")
        print(df["Age"].head(10))

        # coerce -> Invalid value gets converted as NaN 
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")       

        age_median = df["Age"].median()

        # Replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("Age column after pre-processing : ")
        print(df["Age"].head(10))

    # Handel Fare column 
    if "Fare" in df.columns:
        print("\nFare column before pre-processing")
        print(df["Fare"].head(10))

        # coerce -> Invalid value gets converted as NaN 
        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")

        fare_median = df["Fare"].median()

        print("\nMedian of Fare column is : ",fare_median)

        # Replace missing values with median
        df["Fare"] = df["Fare"].fillna(fare_median)

        print("Fare column after pre-processing : ")
        print(df["Fare"].head(10))

    # Handel Embarked column
    if "Embarked" in df.columns:
        print("\n Embarked column before pre-processing")
        print(df["Embarked"].head(10))

        # Convert the data into string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # Remove missing values
        df["Embarked"] = df["Embarked"].replace(['nan','None',''],np.nan)

        # Get most frequent value
        embarked_mode = df["Embarked"].mode()[0]
        print("Mode of Embarked column : ",embarked_mode)

        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("Embarked column after pre-processing : ")
        print(df["Embarked"].head(10))

    # Handel Sex column 
    if "Sex" in df.columns:
        print("\Sex column before pre-processing")
        print(df["Sex"].head(10))

        # coerce -> Invalid value gets converted as NaN 
        df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")

        print("Sex column after pre-processing : ")
        print(df["Sex"].head(10))

    
    DisplayInfo("Data after pre-processing")
    print(df.head())

    print("\nMissing values after pre-processing")
    print(df.isnull().sum())


    return df

#----------------------------------------------------------------
#   Function name : MarvellousTitanicLogistic
#   Description :   This is main Pipe Line controller
#                   It Loads the datasets, show raw data
#                   It pre-Process the dataset & tain the model
#   Parameters :    Data Path of dataset file
#   Return :        None
#   Date :          14/03/2026
#   Author :        Sanket Sadashiv Hajare
#----------------------------------------------------------------

def MarvellousTitanicLogistic(datapath):
    DisplayInfo("Step 1 : Loading the dataset")
    df = pd.read_csv(datapath)

    ShowData(df,"Initial dataset")

    df = CleanTitanicData(df)


#----------------------------------------------------------------
#   Function name : main
#   Description :   Starting point of the application
#   Parameters :    None
#   Return :        None
#   Date :          14/03/2026
#   Author :        Sanket Sadashiv Hajare
#----------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("MarvellousTitanicDataset.csv")

if __name__ == "__main__":
    main()