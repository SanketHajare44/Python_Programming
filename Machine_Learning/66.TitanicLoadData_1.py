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